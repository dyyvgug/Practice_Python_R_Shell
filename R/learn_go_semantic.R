if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("GOSemSim")
BiocManager::install("org.Hs.eg.db")
library(GOSemSim)
library(org.Hs.eg.db)
library(tidyverse)
#https://yulab-smu.top/biomedical-knowledge-mining-book/GOSemSim.html

hsGO <- godata('org.Hs.eg.db', ont="MF")
# one gene pairs,ENTREZID
o = GOSemSim::geneSim("241", "251", semData=hsGO, measure="Wang", combine="BMA")
print(o)
# by gene name
o2 = GOSemSim::geneSim("CDC45", "MCM10", semData=hsGO2, measure="Wang", combine="BMA")
v = o2[1]
print(v)
n = as.character(v)
print(n)

# ----------------------------------------------------------------------------------
# a string of genes
# ----------------------------------------------------------------------------------
s = mgeneSim(genes=c("835", "5261","241", "994"),
         semData=hsGO, measure="Wang",verbose=FALSE)
print(s)
# with gene name
hsGO2 <- godata('org.Hs.eg.db', keytype = "SYMBOL", ont="MF", computeIC=FALSE) 
genes <- c("CDC45", "MCM10", "CDC20", "NMU", "MMP1")
s2 <- mgeneSim(genes, semData=hsGO2, measure="Wang", combine="BMA", verbose=FALSE)
print(s2)

# transform the matrix to a table
m_t <- read.table(text = s2, header = TRUE) %>%
  as.data.frame()

m_t %>%
  pivot_longer(-1, names_to = "col2", values_to = "value") %>%
  filter(col1 < col2) %>%  # Filter for unique pairs
  select(col1, col2, value) 
print(m_t)

# --------------------------------------------------------------------------------
# cluster
# --------------------------------------------------------------------------------
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
