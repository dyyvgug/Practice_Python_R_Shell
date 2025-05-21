"""
Fetch the current HGNC master table and keep only
  • 'symbol'  (approved HGNC gene symbol, 2025 snapshot)
  • 'ensembl_gene_id'  (corresponding ENSG)
Outputs: hgnc_symbol_ensembl_YYYYMMDD.tsv
"""

import pandas as pd
import requests
from pathlib import Path
from datetime import date
import io, gzip

# ------------------------------------------------------------------
# 1. Download the latest “complete set” from the HGNC FTP mirror
#    (it is ~6 MB gzip, updated weekly)
# ------------------------------------------------------------------
HGNC_URL = (
    "https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/"
    "hgnc_complete_set.txt.gz"
)
gz_bytes = requests.get(HGNC_URL, timeout=60).content
tsv_bytes = gzip.decompress(gz_bytes)

# ------------------------------------------------------------------
# 2. Load into a DataFrame (tab-separated with header row)
# ------------------------------------------------------------------
df = pd.read_csv(io.BytesIO(tsv_bytes), sep="\t", low_memory=False)

# ------------------------------------------------------------------
# 3. Keep only SYMBOL ↔ ENSG columns, drop rows lacking ENSG
# ------------------------------------------------------------------
out_df = (
    df[["symbol", "ensembl_gene_id"]]
      .dropna(subset=["ensembl_gene_id"])
      .astype(str)
      .drop_duplicates()
      .sort_values("symbol")
      .reset_index(drop=True)
)

print(f"{len(out_df):,} rows with approved symbol + ENSG …")

# ------------------------------------------------------------------
# 4. Save to disk
# ------------------------------------------------------------------
today = date.today().strftime("%Y%m%d")
out_path = Path(f"hgnc_symbol_ensembl_{today}.tsv")
out_df.to_csv(out_path, sep="\t", index=False)
print(f"Saved: {out_path.resolve()}")

