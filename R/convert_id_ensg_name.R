# ===================================================================
# Yingying Dong.convert gene name,ID,ENSG
# ===================================================================
if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("topGO")
library(topGO)
BiocManager::install("clusterProfiler")
library(clusterProfiler)
BiocManager::install("AnnotationHub")
# if the species is human,use the org.Hs.eg.db
BiocManager::install("org.Hs.eg.db")
library(AnnotationHub)
library(org.Hs.eg.db)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
hub = AnnotationHub()
unique(hub$species)
spe = "Homo sapiens"
hub$species[which(hub$species == spe)]
query(hub,spe)
hub[hub$species == spe &hub$rdataclass == 'OrgDb']
OrgDb = hub[["AH95959"]] #human
keytypes(OrgDb)
keytypes(org.Hs.eg.db)
#==============================================================================================
# Import data and conversion id
#==============================================================================================
ensg <- read.table("ensg.txt",header = F,sep = '\t')
ensids <- c("ENSG00000130720", "ENSG00000103257", "ENSG00000156414", 
            "ENSG00000144644", "ENSG00000159307", "ENSG00000144485")
# method 1
cols <- c("SYMBOL", "GENENAME")
table <- select(org.Hs.eg.db, keys=ensids, columns=cols, keytype="ENSEMBL")
# method 2
symbol <- bitr(ensids,'ENSEMBL','SYMBOL',OrgDb)
head(symbol)
ensg <- bitr(ensp,'ENSEMBLPROT','ENTREZID',OrgDb)
head(ensg)
write.table(symbol,"symbol.txt",sep = '\n',quote = F,col.names = F,row.names = F)


