# ggplot2 add straight lines to a plot 
###################### geom_hline : Add horizontal lines ###########################
library(ggplot2)
# Simple scatter plot
sp <- ggplot(data=mtcars, aes(x=wt, y=mpg)) + geom_point()
# Add horizontal line at y = 2O
sp + geom_hline(yintercept=20)
# Change line type and color
sp + geom_hline(yintercept=20, linetype="dashed", color = "red")
# Change line size
sp + geom_hline(yintercept=20, linetype="dashed", 
                color = "red", size=2)
##################### geom_vline : Add vertical lines #############################
# Add a vertical line at x = 3
sp + geom_vline(xintercept = 3)
# Change line type, color and size
sp + geom_vline(xintercept = 3, linetype="dotted", 
                color = "blue", size=1.5)
##################### geom_abline : Add regression lines ##########################
# Fit regression line
require(stats)
reg<-lm(mpg ~ wt, data = mtcars)
reg
coeff=coefficients(reg)
# Equation of the line : 
eq = paste0("y = ", round(coeff[2],1), "*x + ", round(coeff[1],1))
# Plot
sp + geom_abline(intercept = 37, slope = -5)+
  ggtitle(eq)
# Change line type, color and size
sp + geom_abline(intercept = 37, slope = -5, color="red", 
                 linetype="dashed", size=1.5)+
  ggtitle(eq)
#Note that, the function stat_smooth() can be used for ->fitting smooth models to data.
sp + stat_smooth(method="lm", se=FALSE,linetype="dashed", color = "blue",size = 0.75)
##################### geom_segment : Add a line segment ##############################
# Add a vertical line segment
sp + geom_segment(aes(x = 4, y = 15, xend = 4, yend = 27))
# Add horizontal line segment
sp + geom_segment(aes(x = 2, y = 15, xend = 3, yend = 15))
#Note that, you can add an arrow at the end of the segment. grid package is required.
library(grid)
sp + geom_segment(aes(x = 5, y = 30, xend = 3.5, yend = 25),
                  arrow = arrow(length = unit(0.5, "cm")))
