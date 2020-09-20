library(readxl)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path)) #RStudio中设置当前源文件目录作为工作目录
list.files(getwd())
t = list.files(getwd(),pattern = '*.[T.txt]$')
t
cdir = setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
a = read_excel('aggregate.xlsx',sheet=1)
names(a) = c("food","food2","sales","money")
agg = aggregate(money~food, data=a, FUN=sum)
agg2 <- aggregate(money~food+food2, data=a, FUN=sum)