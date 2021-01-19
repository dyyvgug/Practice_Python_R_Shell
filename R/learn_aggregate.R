# learning aggregate(). Yingying Dong.
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
df <- chickwts
head(df)
# ==================================================================
# FUN, mean
# ==================================================================
group_mean <- aggregate(df$weight, list(df$feed), mean)
group_mean <- aggregate(weight ~ feed, data = df, mean) # Equivalent
group_mean
colnames(group_mean) <- c("Group", "Mean")
# ==================================================================
# FUN, count
# ==================================================================
group_count <- aggregate(df$feed, by = list(df$feed), FUN = length)
group_count <- aggregate(feed ~ feed, data = df, FUN = length) #Equivalent
group_count
# ==================================================================
# FUN, quantile
# a time series object of class xts
# Sample xts object
# ==================================================================
library(lubridate)
set.seed(1)
Dates <- seq(dmy("01/01/2020"), dmy("01/01/2021"), by = "day")
Return <- rnorm(length(Dates))

library(xts)
tserie <- xts(Return, Dates)
head(tserie)
# calculating the quantiles 5% and 95% for the returns of each month typing.
dat <- aggregate(tserie ~ month(index(tserie)), FUN = quantile,
                 probs = c(0.05, 0.95))
colnames(dat)[1] <- "Month"
dat
# ==================================================================
# Aggregate by multiple columns
# ==================================================================
set.seed(1)

cat_var <- sample(c("A","B","C"), nrow(df),replace = TRUE)
df2 <- cbind(df, cat_var)
head(df2)

aggregate(df2$weight, by = list(df2$feed, df2$cat_var), FUN = sum)
aggregate(weight ~ feed + cat_var, data = df2, FUN = sum) # Equivalent

# two or more numerical variables
set.seed(1)
num_var <- rnorm(nrow(df))
df3 <- cbind(num_var, df)
head(df3)
# two or more numerical variables, we can use cbind()
aggregate(cbind(df3$num_var, df3$weight),list(df3$feed),mean)
