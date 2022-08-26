# R write add
for(i in 1:50){
  ff <- file("TRY.txt",open="at")
  write.table(i,file=ff)
  close(ff)
}
for(i in 1:50){
  write.table(i,file="try2.txt",append = T,quote = F,col.names=!file.exists("try2.txt"))
}