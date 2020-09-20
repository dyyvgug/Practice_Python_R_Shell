# ggplot2 axis scales and transformations
################################# Prepare the data ###################################
# Convert dose column dose from a numeric to a factor variable
ToothGrowth$dose <- as.factor(ToothGrowth$dose)
head(ToothGrowth)
library(ggplot2)
# Box plot 
bp <- ggplot(ToothGrowth, aes(x=dose, y=len)) + geom_boxplot()
bp
# scatter plot
sp<-ggplot(cars, aes(x = speed, y = dist)) + geom_point()
sp
# Box plot : change y axis range
bp + ylim(0,50)
# scatter plots : change x and y limits
sp + xlim(5, 40)+ylim(0, 150)
# set the intercept of x and y axis at (0,0)
sp + expand_limits(x=0, y=0)
# change the axis limits
sp + expand_limits(x=c(0,30), y=c(0, 150))
# Change x and y axis labels, and limits
sp + scale_x_continuous(name="Speed of cars", limits=c(0, 30)) +
  scale_y_continuous(name="Stopping distance", limits=c(0, 150))
# Default scatter plot
sp <- ggplot(cars, aes(x = speed, y = dist)) + geom_point()
sp
# Log transformation using scale_xx()
# possible values for trans : 'log2', 'log10','sqrt'
sp + scale_x_continuous(trans='log2') +
  scale_y_continuous(trans='log2')
# Sqrt transformation
sp + scale_y_sqrt()
# Reverse coordinates
sp + scale_y_reverse() 
# Possible values for x and y : "log2", "log10", "sqrt", ...
sp + coord_trans(x="log2", y="log2")
###################### Format axis tick mark labels #########################
# Log2 scaling of the y axis (with visually-equal spacing)
library(scales)
sp + scale_y_continuous(trans = log2_trans())
# show exponents
sp + scale_y_continuous(trans = log2_trans(),
                        breaks = trans_breaks("log2", function(x) 2^x),
                        labels = trans_format("log2", math_format(2^.x)))
#Note that many transformation functions are available using the scales package : log10_trans(), sqrt_trans(), etc. Use help(trans_new) for a full list.
# Percent
sp + scale_y_continuous(labels = percent)
# dollar
sp + scale_y_continuous(labels = dollar)
# scientific
sp + scale_y_continuous(labels = scientific)
########################## Display log tick marks #######################
library(MASS)
head(Animals)
# x and y axis are transformed and formatted
p2 <- ggplot(Animals, aes(x = body, y = brain)) + geom_point() +
  scale_x_log10(breaks = trans_breaks("log10", function(x) 10^x),
                labels = trans_format("log10", math_format(10^.x))) +
  scale_y_log10(breaks = trans_breaks("log10", function(x) 10^x),
                labels = trans_format("log10", math_format(10^.x))) +
  theme_bw()
# log-log plot without log tick marks
p2
# Show log tick marks
p2 + annotation_logticks()  
# Log ticks on left and right
p2 + annotation_logticks(sides="lr")
# All sides
p2+annotation_logticks(sides="trbl")
########################### Format date axes #############################
df <- data.frame(
  date = seq(Sys.Date(), len=100, by="1 day")[sample(100, 50)],
  price = runif(50)
)
df <- df[order(df$date), ]
head(df)
# Plot with date
dp <- ggplot(data=df, aes(x=date, y=price)) + geom_line()
dp
library(scales)
# Format : month/day
dp + scale_x_date(labels = date_format("%m/%d")) +
  theme(axis.text.x = element_text(angle=45))
# Format : Week
dp + scale_x_date(labels = date_format("%W"))
# Months only
dp + scale_x_date(breaks = date_breaks("months"),
                  labels = date_format("%b"))
############################ Date axis limits ##################################
head(economics)
# Plot with dates
dp <- ggplot(data=economics, aes(x=date, y=psavert)) + geom_line()
dp
# Axis limits c(min, max)
min <- as.Date("2002-1-1")
max <- max(economics$date)
dp+ scale_x_date(limits = c(min, max))
# the function scale_x_datetime() and scale_y_datetime() to plot a data containing date and time.
