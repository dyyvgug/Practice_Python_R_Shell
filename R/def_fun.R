## --------------------------------
## merge CAI and FPKM
## --------------------------------
setwd("/media/hp/disk1/DYY/reference/annotation/")

species = "Apis_mellifera"
outcomes = function (species, threshold)  {
  cbi  = read.table(paste(species, "/ref/CBI_CAI.txt", threshold, sep = ""), 
                    sep = "\t", header = T)
  setwd(paste("/media/hp/Katniss/DYY/aligned/",species,sep = ""))
  gtf_array = list.files(getwd(),pattern = "\\d.+[txt]$")
  gtf_array
  gtf = read.table(file.choose(gtf_array), sep = "\t", header=F)
  gtf = gtf [ , apply(gtf, 2, function(x) !any(is.na(x)))]  # remove columns have NA
  df = merge(cbi, gtf, by.x = "transcription_id", 
             by.y = "V1")
  cor = cor.test(df$CAI, log2(df$V3))
  jpeg(paste("/media/hp/disk1/DYY/reference/CAI_CBI_FT/",species,"/FPKM/out.jpg"), 
       width = 480, height = 480, quality = 100)
  plot(df$CAI, df$V3, log = "y", pch = 16, col = "cyan",
       cex = 0.5, main = "round(cor$estimate, 2)" )
  
  dev.off()
}



## --------------------------------
## merge CAI and TPM
## --------------------------------


sample = paste0("arabidopsis", 1:10)
sample

for (i in sample)   {
  a = cal.cor(i, 0.5)
}



