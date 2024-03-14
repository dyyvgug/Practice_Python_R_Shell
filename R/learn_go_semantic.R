if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("GOSemSim")
BiocManager::install("org.Hs.eg.db")
library(GOSemSim)
library(org.Hs.eg.db)
#https://yulab-smu.top/biomedical-knowledge-mining-book/GOSemSim.html

hsGO <- godata('org.Hs.eg.db', ont="MF")
# one gene pairs,ENTREZID
o = GOSemSim::geneSim("241", "251", semData=hsGO, measure="Wang", combine="BMA")
print(o)
# a string of genes
s = mgeneSim(genes=c("835", "5261","241", "994"),
         semData=hsGO, measure="Wang",verbose=FALSE)
print(s)
# with gene name
hsGO2 <- godata('org.Hs.eg.db', keytype = "SYMBOL", ont="MF", computeIC=FALSE) 
genes <- c("CDC45", "MCM10", "CDC20", "NMU", "MMP1")
name <- mgeneSim(genes, semData=hsGO2, measure="Wang", combine="BMA", verbose=FALSE)
print(name)
# cluster
gs1 <- c("835", "5261","241", "994", "514", "533")
gs2 <- c("578","582", "400", "409", "411")
c1 <- clusterSim(gs1, gs2, semData=hsGO, measure="Wang", combine="BMA")
print(c1)
#three clusters
x <- org.Hs.egGO
hsEG <- mappedkeys(x)
set.seed <- 123
clusters <- list(a=sample(hsEG, 20), b=sample(hsEG, 20), c=sample(hsEG, 20))
c2<-mclusterSim(clusters, semData=hsGO, measure="Wang", combine="BMA")
print(c2)
