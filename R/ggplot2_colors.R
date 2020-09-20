#=============================Prepare the data================================================
# Convert dose and cyl columns from numeric to factor variables
ToothGrowth$dose <- as.factor(ToothGrowth$dose)
mtcars$cyl <- as.factor(mtcars$cyl)
head(ToothGrowth)
head(mtcars)
#===================================Simple plots==============================================
library(ggplot2)
# Box plot
ggplot(ToothGrowth, aes(x=dose, y=len)) +geom_boxplot()
# scatter plot
ggplot(mtcars, aes(x=wt, y=mpg)) + geom_point()
#==================================Use a single color==========================================
# box plot
ggplot(ToothGrowth, aes(x=dose, y=len)) +
  geom_boxplot(fill='#A4A4A4', color="darkred")
# scatter plot
ggplot(mtcars, aes(x=wt, y=mpg)) + 
  geom_point(color='darkblue')
#=================================Change colors by groups======================================
# Box plot
bp<-ggplot(ToothGrowth, aes(x=dose, y=len, fill=dose)) +
  geom_boxplot()
bp
# Scatter plot
sp<-ggplot(mtcars, aes(x=wt, y=mpg, color=cyl)) + geom_point()
sp
# The lightness (l) and the chroma (c, intensity of color) of the default (hue) colors can be modified using the functions scale_hue.
# Note that, the default values for l and c are : l = 65, c = 100.
# Box plot
bp + scale_fill_hue(l=40, c=35)
# Scatter plot
sp + scale_color_hue(l=40, c=35)
# Box plot
bp + scale_fill_manual(values=c("#999999", "#E69F00", "#56B4E9"))
# Scatter plot
sp + scale_color_manual(values=c("#999999", "#E69F00", "#56B4E9"))
# Box plot
bp + scale_fill_manual(breaks = c("2", "1", "0.5"), 
                       values=c("red", "blue", "green"))
# Scatter plot
sp + scale_color_manual(breaks = c("8", "6", "4"),
                        values=c("red", "blue", "green"))
#==============================Use RColorBrewer palettes======================================
# Box plot
bp + scale_fill_brewer(palette="Dark2")
# Scatter plot
sp + scale_color_brewer(palette="Dark2")
#==============================Use Wes Anderson color palettes================================
# Install
install.packages("wesanderson")
# Load
library(wesanderson)
library(wesanderson)
# Box plot
bp+scale_fill_manual(values=wes_palette(n=3, name="Royal1"))
# Scatter plot
sp+scale_color_manual(values=wes_palette(n=3, name="Royal2"))
#==================================Use gray colors============================================
# Box plot
bp + scale_fill_grey() + theme_classic()
# Scatter plot
sp + scale_color_grey() + theme_classic()
# Change the gray value at the low and the high ends of the palette
# Note that, the default value for the arguments start and end are : start = 0.2, end = 0.8
# Box plot
bp + scale_fill_grey(start=0.8, end=0.2) + theme_classic()
# Scatter plot
sp + scale_color_grey(start=0.8, end=0.2) + theme_classic()
#================================Continuous colors============================================
#==========================Gradient colors for scatter plots==================================
# Color by qsec values
sp2<-ggplot(mtcars, aes(x=wt, y=mpg, color=qsec)) + geom_point()
sp2
# Change the low and high colors
# Sequential color scheme
sp2+scale_color_gradient(low="blue", high="red")
# Diverging color scheme
mid<-mean(mtcars$qsec)
sp2+scale_color_gradient2(midpoint=mid, low="blue", mid="white",
                          high="red", space ="Lab" )
#=======================Gradient colors for histogram plots====================================
#Note that, the functions scale_color_continuous() and scale_fill_continuous() can be used also to set gradient colors.
set.seed(1234)  #Set the seed of the random number
x <- rnorm(200) #Under the premise of setting seeds,generating 200 random numbers subject to a normal distribution
# Histogram
hp<-qplot(x =x, fill=..count.., geom="histogram") 
hp
# Sequential color scheme
hp+scale_fill_gradient(low="blue", high="red")
#===============================Gradient between n colors=======================================
# Scatter plot
# Color points by the mpg variable
sp3<-ggplot(mtcars, aes(x=wt, y=mpg, color=mpg)) + geom_point()
sp3
# Gradient between n colors
sp3+scale_color_gradientn(colours = rainbow(5))
