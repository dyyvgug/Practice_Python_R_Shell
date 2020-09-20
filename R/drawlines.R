
#!/usr/bin/env Rscript

## take the arguments from environment
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)}


sam = args[1]

library(reshape2)
library(ggplot2)
setwd(getwd())

draw.lines = function (sam, pos)    {
  
  # work on true 
  dt = read.table(paste(sam, "/classify/gc_", pos, "_true.csv", sep = ""), 
                  sep = "\t", header = T)
  dt1 = as.data.frame(t(apply(dt[,2:5], 1, function(x) x/sum(x))))
  dt1$pos = dt$pos
  dt1 = melt(dt1, id.vars = "pos")  # melt the data with pos column
  dt1 = dt1[order(-dt1$pos),]
  names(dt1) = c("position", "base", "frequency")
#name(),name vectors.  
  p = ggplot(dt1, aes(position, frequency, group = base)) + 
    geom_line(aes(color=base)) + 
    theme_bw() + 
    theme(panel.border = element_blank(), panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
 
  p+xlab('position')+ylab('base frequency')+
    ggtitle(paste(sam, pos, "true PAS GC content"))+ylim(c(0,1))
  #scale_x_continuous(breaks = seq(-(ncol(dt1)-6)/2, (ncol(dt1)-1)/2, by = 10))+
  #scale_y_continuous(breaks = seq(0,1,0.25))
  
  
  ggsave(filename = paste(sam,"/classify/gc_", pos, "_true.eps",sep = ""), plot = last_plot(), device = "eps",
         width = 10, height = 4, units = "in", dpi = 300)
  
  
  # work on false
  df = read.table(paste(sam, "/classify/gc_", pos, "_false.csv", sep = ""), 
                  sep = "\t", header = T)
  df1 = as.data.frame(t(apply(df[,2:5], 1, function(x) x/sum(x))))
  df1$pos = df$pos
  df1 = melt(df1, id.vars = "pos")  # melt the data with pos column
  df1 = df1[order(-dt1$pos),]
  names(df1) = c("position", "base", "frequency")
  #df1 = dt1[grep("A|T", dt1$base),]
  
  p = ggplot(df1, aes(position, frequency, group = base)) + 
    geom_line(aes(color=base)) + 
    theme_bw() + 
    theme(panel.border = element_blank(), panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
  
  p+xlab('position')+ylab('base frequency')+
    ggtitle(paste(sam, pos, "false PAS GC content"))+ylim(c(0,1))
  #scale_x_continuous(breaks = seq(-(ncol(dt1)-6)/2, (ncol(dt1)-1)/2, by = 10))+
  #scale_y_continuous(breaks = seq(0,1,0.25))
  
  ggsave(filename = paste(sam,"/classify/gc_", pos, "_false.eps",sep = ""), plot = last_plot(), device = "eps",
         width = 10, height = 4, units = "in", dpi = 300)
  
  
  # compare A/T between T and F
  
  df1 = df1[grep("A|T", df1$base),]
  dt1 = dt1[grep("A|T", dt1$base),]
  
  dt1$base = paste("True", dt1$base)
  
  df1$base = paste("False", df1$base) 
  
  
  df = rbind(dt1, df1)
  
  p = ggplot(df, aes(position, frequency, group = base)) + 
    geom_line(aes(color=base)) + 
    theme_bw() + 
    theme(panel.border = element_blank(), panel.grid.major = element_blank(),
          panel.grid.minor = element_blank(), axis.line = element_line(colour = "black"))
  
  p+xlab('position')+ylab('base frequency')+
    ggtitle(paste(sam, pos, "false vs true PAS AT content"))+ylim(c(0,1))
  
  
  ggsave(filename = paste(sam,"/classify/AT_", pos, "_true vs false.eps",sep = ""), plot = last_plot(), device = "eps",
         width = 10, height = 4, units = "in", dpi = 300)
  
  
}






### ========================================
##  PAS Codon frequency and HEATMAP
### ========================================

dir.create("classify_PAS")
dir.create(paste("classify_PAS/", sam, sep = "" ))


intup = function(x) {
  d = t.test(x)
  d$conf.int[2]
}

intdn = function(x)  {
  d = t.test(x)
  d$conf.int[1]
}


pas.heatmap = function(sam, up, dn, st, ed, out)  {
  
  cf = read.table(paste(sam, "/classify/codon_", up, ".UP_", dn,
                        ".Down_PAS_T.txt", sep = ""), sep = "\t", fill = T)
  rpm = read.table(paste(sam, "/CDS_UTR_PolyA_counts.txt", sep = ""), sep = "\t", header = T)
  rpm = rpm[,1:3]
  cf = merge(rpm, cf, by.x = "Gene", by.y = "V2")
  df = cf
  
  #make a table to compare the composition of codons 
  x = as.data.frame(table(df$V5))
  names(x) = c("codon", "P1")
  column = 5:(ncol(df)-3)
  for (i in column)  {
    cl = paste("V", i, sep = "")
    cl2 = paste("P", i-3, sep = "")
    d1 = as.data.frame(table(df[[cl]]))
    names(d1) = c("codon", cl2)
    x = merge(x, d1, by.x = "codon", by.y = "codon", all = T)
  }
  #for(),creat a loop for column seqencings count "v",'p".
  x[is.na(x)] = 0
  x = x[!(x$codon %in% c("TGA", "TAA", "TAG", "")),]
  x$sAll = apply(x[,2:ncol(x)], 1, sum)
  select = x[x$sAll > 1*(ncol(x)-2), ]
  
  
  
  ## draw control
  ck = read.table(paste(sam, "/classify/codon_", up, ".UP_", dn,
                        ".Down_PAS_F.txt", sep = ""), sep = "\t", fill = T)
  ck = na.omit(ck)
  ck = ck[ck$V2 %in% df$Gene,]  # gene used for analyses must be the same group as having internal cleavage
  x1 = as.data.frame(table(ck$V3))
  names(x1) = c("codon", "P1")
  column = 3:ncol(ck)
  for (i in column)  {
    cl = paste("V", i, sep = "")
    cl2 = paste("P", i-1, sep = "")
    d1 = as.data.frame(table(ck[[cl]]))
    names(d1) = c("codon", cl2)
    x1 = merge(x1, d1, by.x = "codon", by.y = "codon", all = T)
  }
  x1[is.na(x1)] = 0
  x1$ckAll = apply(x1[,2:ncol(x1)], 1, sum)
  x1 = x1[x1$codon %in% x$codon,]
  
  
  m1 = as.matrix(x[,2:(ncol(x)-1)]) 
  row.names(m1) = x$codon
  m1 = m1/max(m1)
  m2 = as.matrix(x1[,2:(ncol(x)-1)])
  row.names(m2) = x1$codon
  m2 = m2/max(m2)
  
  mat = log2(m1/m2)
  mat[is.na(mat)] = 0
  mat[is.infinite(mat)] = max(mat[is.finite(mat)])
  
  ### ----------------------------------------------------
  ### This part draw codon frequency by amino acid level
  ### ----------------------------------------------------
  
  df = merge(x, x1, by.x = "codon", by.y = "codon")
  df$sAll = df$sAll/sum(df$sAll) 
  ref = read.table("ref/CBI_ref.txt", sep = "\t", header = T)
  df = merge(ref, df, by.x = "codon", by.y = "codon")
  ref = read.table("ref/codon_frequency.txt", sep = "\t")
  ref = ref[,-2]
  df = merge(ref, df, by.x = "V1", by.y = "codon")
  
  names(df)[1:2] = c("codon", "frequency")
  v = st:ed # region, i.e. number of first n codon (from st to end, for example 1 to 6 codon from left)
  exclude = up:(up+2) # do not count the 
  v = v[! v %in% exclude]
  ve = paste("P", v, ".x", sep = "")
  df$sum = apply(df[,ve], 1, sum)
  df = df[df$sum > 0, ]
  df$sum = df$sum/sum(df$sum)
  df$frequency = df$frequency/sum(df$frequency)
  df$ratio = log2(df$sum/df$frequency)
  
  
  df = df[order(df$AA, -df$CAI),]
  
  
  ## -------------------------
  # draw dotplot
  
  
  
  setEPS()
  if (out == "eps")   {
    postscript(paste("classify_PAS/", sam, "/P", st, "-", ed, " flanking PAS dot.eps", sep=""), pointsize =15)
  }else{
    jpeg(filename = paste("classify_PAS/", sam, "/P", st, "-", ed, " flanking PAS dot.jpeg", sep=""),
         width = 600, height = 1200, units = "px", quality = 100)   }
  
  par(mfrow = c(1,1))
  #df1 = df
  df1 = df[df$codon %in% select$codon,]
  
  cor = cor.test(df1$CAI, df1$ratio)
  plot(df1$CAI, df1$ratio, main = sam, xlab = "CAI", ylab = "normalized codon frequency (log2)", pch = 16, col = "dodgerblue3")
  l = lm(df1$ratio~df1$CAI)
  abline(l, col = "red", lty = 3, lwd = 3)
  text(max(df1$CAI)-0.2, max(df1$ratio)-0.5, paste(" r =", round(cor$estimate, 3), "\n n =", 
                                                   nrow(df1), "\n P=", formatC(cor$p.value, digits = 3)))
  
  dev.off()
  
  ##-------------------
  ## draw multiple tiles 
  
  if (out == "eps")   {
    postscript(paste("classify_PAS/", sam, "/P", st, "-", ed, " flanking PAS ratio codon.eps", sep=""), pointsize =5,
               width = 4, height = 8)
  }else{
    jpeg(filename = paste("classify_PAS/", sam, "/P", st, "-", ed, " flanking PAS ratio codon.jpeg", sep=""), 
         width = 600, height = 1200, units = "px", quality = 100)      }
  
  par(mar=c(4,2,2,2))
  par(mfrow=c(6,3),tcl=-0.5,mai=c(0.4,0.2,0.1,0.2))  #mar set the margin from bottom, left, top, right
  
  aa <- c("A","C","D","E","F","G","H","I","K","L","N","P","Q","R","S","T","V","Y")
  
  df$color = "darkseagreen1"
  df$color[df$codon %in% df1$codon] = "grey70"
  
  for (i in aa) {
    
    n = nrow(df[df$AA == i,])
    n = ifelse(n = 2, 2.5, n) 
    min = min(df$ratio[df$AA == i])
    min = ifelse(min>0, -0.2, min-0.2)
    max = max(df$ratio[df$AA == i])
    max = ifelse(max>0, max+0.2, 0.1)
    
    mp<-barplot(t(df[df$AA == i, "ratio"]),ann=FALSE, names.arg = df$codon[df$AA == i], 
                cex.names = 1.2, main = i, las = 2, #axes = F,
                ylim = c(min, max), 
                col = df$color[df$AA == i] ,xlim = c(0,n), width=c(0.5,0.5,0.5), space = 0.8)
    par(new = T)
    abline(h = 0, col = "cyan", lwd = 2, lty = 2)
    par(new = T)
    plot(mp,df$CAI[df$AA == i],type="b",lwd = 2,col="red", xlim = c(0,n), ylim = c(0,1.2), ann=FALSE, axes = F)
    axis(4,at=seq(0,1.2,0.2))
    
    box()   
  }
  dev.off() 
  
  
  
  ### ------------------------------
  #report relative changes to control in heatmap 
  ### ------------------------------
  library(pheatmap)
  jpeg(filename = paste("classify_PAS/", sam, "/flanking PAS codon relative frequency.jpg", sep = ""),
       width = 800, height = 1200, units = "px", quality = 100)
  
  pheatmap(mat, clustering_distance_rows = 'euclidean',  #option is correlation', 'euclidean', 'maximum', 'manhattan', 'canberra', 'binary', 'minkowski'
           border_color = NA, cluster_rows = T, annotation_names_row = T, annotation_names_col = T, show_rownames = T, cluster_cols = F, silent = F,
           annotation_row = NA, fontsize_row = 17, fontsize_col = 22, fontsize = 14)
  
  dev.off() 
  
  # report codon frequency changes 
  jpeg(filename = paste("classify_PAS/", sam, "/flanking PAS codon frequency.jpg", sep = ""),
       width = 800, height = 1200, units = "px", quality = 100)
  
  pheatmap(m1, clustering_distance_rows = 'euclidean',  #option is correlation', 'euclidean', 'maximum', 'manhattan', 'canberra', 'binary', 'minkowski'
           border_color = NA, cluster_rows = T, annotation_names_row = T, annotation_names_col = T, show_rownames = T, cluster_cols = F, silent = F,
           annotation_row = NA, fontsize_row = 17, fontsize_col = 22, fontsize = 14)
  dev.off() 
  
  # report random codon frequency changes 
  jpeg(filename = paste("classify_PAS/", sam, "/flanking PAS codon random frequency.jpg", sep = ""),
       width = 800, height = 1200, units = "px", quality = 100)
  
  pheatmap(m2, clustering_distance_rows = 'euclidean',  #option is correlation', 'euclidean', 'maximum', 'manhattan', 'canberra', 'binary', 'minkowski'
           border_color = NA, cluster_rows = T, annotation_names_row = T, annotation_names_col = T, show_rownames = T, cluster_cols = F, silent = F,
           annotation_row = NA, fontsize_row = 17, fontsize_col = 22, fontsize = 14)
  dev.off() 
  
}





positions = c("CDS", "CDS_intron", "UTR")

for( s in positions)  {
  draw.lines(sam, s )
}

pas.heatmap(sam,0,15,3,17, "eps")
#pas.heatmap(sam,0,15,18,32,"eps")
#pas.heatmap(sam,0,15,1,32,"eps")