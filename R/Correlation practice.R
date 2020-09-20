# Correlation practice
#==============================================================================
# Part 1 plot
#==============================================================================
data(Capm,package="Ecdat")
head(Capm,3)
# Plot food sector excess returns versus market excess returns using plot function
plot(Capm[,"rmrf"]/100,Capm[,"rfood"]/100,ylab="Food industry excess return",
     xlab="Market excess return",pch=19,col=rgb(0,0,100,50,maxColorValue=255))
# Plot pair plots of returns
cor(Capm/100)
plot(Capm/100,pch=19,col=rgb(0,0,100,50,maxColorValue=255))
# Moreover, specifying col=rainbow(n, end=0.9) in scatter plots allows one to see the changing relationship over time. The rainbow() function creates a vector n contiguous colors.
plot(Capm/100,col = rainbow(500,end=0.9),pch=19)
#==============================================================================
# Part 2 lattice,pcaPP and ellipse packages
#==============================================================================
# Plot pair plots of returns using the splom function from the lattice package
library(lattice)
splom(Capm/100,pch=19,col=rgb(0,0,100,50,maxColorValue=255))
pairs(Capm/100,labels=c("Food","Durables","Construction","Market","Risk-free"),
      pch=19,col=rgb(0,0,100,50,maxColorValue=255))
# Plot pair plots of returns using the plotcov function from the pacPP package
library(pcaPP)
plotcov(cor(Capm/100),method1="correlation")
# Plot pair plots of returns using the plotcorr function from the ellipse package
# Also, the plotcorr() allows people to have a upper-triangle, lower-triangle or full correlation matrix on their plots by equaling the type argument to “upper”, “lower” and “full”. 
library(ellipse)
plotcorr(cor(Capm/100),num=T,diag=F,type="full")
#==============================================================================
# Part 3 test statistic
#==============================================================================
# Plot pair plots of returns with test statistic
sig.r <- function(p,n)
   {
    df <- n-2
    t.stat <- qt(p,df)
    sig.r <- t.stat/sqrt(t.stat^2+df)
    return(sig.r)
    }
r.threshold <- sig.r(0.975,4) 
col <- ifelse(cor(Capm/100)>r.threshold,"red",ifelse(cor(Capm/100)< -r.threshold,"yellow","blue"))
plotcorr(cor(Capm/100),col=col,diag=F,cex.lab=0.75,type="upper",numbers=F)
# Compare sample correlation matrix with robust correlation matrix
library(robust)
cor.sample <- cor(Capm/100)
cor.robust <- covRob(Capm/100,cor=T)
plotcov(cov1=cor.sample,cov2=cor.robust,method1="sample",method2="robust")
# The corrgram() function in the corrgram package 
# In the above plot, the directions of slashes in the lower panel divide relationships into two categories, positive and negative. Also, blue denotes positive relationships while pink denotes negative relationships. The darker the colors and the bigger the painted areas are, the stronger the relationships between data.
library(corrgram)
corrgram(Capm/100,labels=c("Food","Durables","Construction","Market","Risk-free"),
         lower.panel=panel.shade,upper.panel=panel.pie,text.panel=panel.txt)
corrgram(Capm/100,labels=c("Food","Durables","Construction","Market","Risk-free"),
         lower.panel=panel.pts, upper.panel=panel.conf, diag.panel=panel.density)
corrgram(Capm/100,labels=c("Food","Durables","Construction","Market","Risk-free"),
         panel=panel.ellipse, text.panel=panel.txt, diag.panel=panel.minmax)
