library(tidyverse)
library(ggpubr)
library(rstatix)
library(reshape)
library(ggplot2)
library(pheatmap)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
df1 <- read.table("carrot_data.txt",header = T)
df <- NULL
df <- log10(df1[,12:ncol(df1)])+1
pca_res <- prcomp(df,scale. = T)
summary(pca_res)
pcs <- predict(pca_res)
pc2 <- data.frame(pcs)

ggplot(pc2, aes(x=PC1, y=PC2, color=df1$BR.1))+
  geom_point()+
  scale_color_manual(values=c('#999999','#E69F00'))

head(df1)
which(df1$BR == 1)
grep("X6",colnames(df1))

scatter.smooth(x=iris$Petal.Length,y = iris$Petal.Width, main="Width ~ Length ")
cor(iris$Petal.Length,  iris$Petal.Width) #Finding Correlation between Petal Length and Width
cor(iris$Petal.Length,  iris$Sepal.Width) #Finding Correlation between Petal Length  and Sepal Width

t.test(iris$Petal.Width,iris$Petal.Length)
linear_model <- lm(Petal.Width ~ Petal.Length, data = iris)
print(linear_model)
summary(linear_model)

coll_GmiFb = read.table("carrot_data_combined_TR.txt",header=TRUE)
coll_GmiFb <- data.frame(coll_GmiFb)

pwc1 <- coll_GmiFb %>%
  group_by(id) %>%
  pairwise_wilcox_test(coll_ol_BR1_n  ~ Geno, p.adjust.method = "bonferroni") 

view(pwc1)

pwc2 <- coll_GmiFb %>%
  group_by(id) %>%
  pairwise_wilcox_test(coll_ol_BR2_n  ~ Geno, p.adjust.method = "bonferroni") 

view(pwc2)
write.table(pwc2,file = "pwc2.txt")
che_table<-read.table("pwc2.txt",sep = "\t",header = T)

#df3 <- reshape(coll_GmiFb,)

test = matrix(rnorm(200), 20, 10)
test[1:10, seq(1, 10, 2)] = test[1:10, seq(1, 10, 2)] + 3
test[11:20, seq(2, 10, 2)] = test[11:20, seq(2, 10, 2)] + 2
test[15:20, seq(2, 10, 2)] = test[15:20, seq(2, 10, 2)] + 4
colnames(test) = paste("Test", 1:10, sep = "")
rownames(test) = paste("Gene", 1:20, sep = "")
head(test)
pheatmap(test)
pheatmap(test, scale = "row")
