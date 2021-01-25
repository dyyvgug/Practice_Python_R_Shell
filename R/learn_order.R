# learning order(). Yingying Dong.

# The numbers are ordered according to its index
y = c(4,12,6,7,2,9,5)
order(y)

# Here the order() will sort the given numbers according to its index in the ascending order. 
# Since number 2 is the smallest, which has an index as five and number 4 is index 1, and similarly, the process moves forward in the same pattern.
y[order(y)]

# ===========================================================
#  Sorting vector using different parameters
# ===========================================================
# order(x,na.last=TRUE)
x <- c(8,2,4,1,-4,NA,46,8,9,5,3)
# Since NA is present, its index will be placed last, where 6 will be placed last because of na.last=TRUE
order(x,na.last = TRUE)
x[order(x,na.last = TRUE)]

# order(x,na.last=FALSE)
order(x,na.last=FALSE)
x[order(x,na.last = FALSE)]

# decreasing=TRUE
order(x,decreasing=TRUE,na.last=TRUE)
x[order(x,decreasing=TRUE,na.last=TRUE)]

# ==========================================================
#  Sorting a dataframe 
# ==========================================================
population = 10
gender = sample(c("male","female"),population,replace = TRUE)
age = sample(25:75,population,replace = TRUE)
degree = sample(c("MA","ME","BE","BSCS"),population,replace = T)
df = data.frame(gender=gender,age=age,degree=degree)
order(df$age)
df[order(df$age),]
