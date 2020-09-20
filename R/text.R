#x<-data.frame(a=I("a\"quote"),b = pi)
#write.table(x,flie ="foo.csv",seq = ",",col.names = NA,qmethod = "double")
          
#x=read.csv(file = "./data/GEO Accession viewer.htm",header = FALSE,skip = 7,sep = "\t")

#2.paste
#s = c("apple","banana","lychee")
#paste(s,"X",seq="_")
#paste(s,collapse = ",")

#3.grep
#library("ALL")
#data(ALL)
#class(ALL$mol.biol)
#negIdx = grep("NEG",ALL$mol.biol)
#negIdx[1:10]

#4.apply
#apply(x,2, mean)
#computes the column means of a matrix x,while

#5.Function
f = function(arg1=10,arg2=20)
{
  print(paste("arg1:",arg1))
  print(paste("arg2:",arg2))
}
f(arg1 = 10,arg2 = 20)

#----------------------------------------------------------
aave =function(x=10)
{
  set.seed(123)        #固定随机数
  tmp=abs(rnorm(10))   #随机正态取值
  xx=0
  for (i in 1:length(tmp)) {
    xx = xx + tmp[i]*i
    print(xx)
    cat("result at",i,"is",xx,"\n")
  }
  xx = sqrt(xx)
  return(xx)
}
aave(10)
#-----------------------------------------------------------
hist(rnorm (10000),breaks =50)

library(MASS)
library(ggplot2) #For the data set
p = ggplot(birthwt,aes(x=factor(race),y=bwt)) + geom_boxplot(notch=TRUE)
p + geom_violin()

#----------------------------------------------------------
?cor
var(1:10)

