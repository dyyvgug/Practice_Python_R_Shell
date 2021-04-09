# Yingying Dong. Gene name to ENSEMBL gene ID.

if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("clusterProfiler")
BiocManager::install("org.Hs.eg.db")
library(clusterProfiler)
library(org.Hs.eg.db)

keytypes(org.Hs.eg.db)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
dir.create("ensgID")
list.files(getwd())
symbol_array = list.files(getwd(),pattern = "*txt$")
symbol_array
for (i in symbol_array) {
  symbol_id = read.table(i, header = F)
  name = sub("^([^.]*).*", "\\1",i)
  symbol_id = as.character(symbol_id$V1)                    
  ensg_id = bitr(symbol_id, fromType="SYMBOL", toType= "ENSEMBL", OrgDb="org.Hs.eg.db")
  head(ensg_id,2)
  only_ensgID = ensg_id[-1]
  write.table(only_ensgID,file = paste0('./ensgID/',name,".txt"),quote = F,
              row.names = F,col.names = F)
}
