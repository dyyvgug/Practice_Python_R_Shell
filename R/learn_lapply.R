# learning lapply(). Yingying Dong.
# applies a function to a list or a vector, returning a list of the same length as the input

# =======================================================================
# iterate over a list
# =======================================================================
a <- list(A = c(8, 9, 7, 5),
          B = data.frame(x = 1:5, y = c(5, 1, 0, 2, 3)))
a
# apply the function sum
lapply(a, sum)

# =======================================================================
# Iterate over a vector
# =======================================================================
# calculate the square root of each element
b <- c(12, 18, 6)
lapply(b, sqrt)
# ======================================================================
# lapply with multiple arguments
# ======================================================================
c <- list(A = c(56, 12, 57, 24), B = c(89, 12, 64, 18, 65, 76))

lapply(c,                           # List
       quantile,                    # Applied function
       probs = c(0.25, 0.5, 0.75))  # Additional argument of the quantile function
# =======================================================================
# lapply with a custom function
# =======================================================================
d <- 1:3
# function to calculate the second power
fun <- function(x){
  x^2
}

# applying our own function
lapply(d, fun)
lapply(d, FUN = function(x) x ^ 2) # equivalent
lapply(d, function(x) x ^ 2) # equivalent

# ========================================================================
# lapply vs for loop
# ========================================================================
# -------------------------- for loop ------------------------------------
# Empty list with 5 elements
x <- vector("list", 5)
vec <- 1:5

for(i in vec){
  if(i %% 2 == 0){ # check if the element 'i' is even or odd
    x[[i]]= i ^ 3
  } else {
    x[[i]] = i ^ 4
  }
}

x
# ------------------------- lapply ----------------------------------------
vec <- 1:5
fun <- function(i){
  if(i %% 2 == 0){
      i ^ 3
  } else {
      i ^ 4
  }
}
lapply(vec, fun)
# ===========================================================================
# lapply vs sapply
# ===========================================================================
# The main difference between the functions is that lapply returns a list instead of an array. 
lapply(c(4, 9, 16), FUN = sqrt)
sapply(c(4, 9, 16), FUN = sqrt)
# However, if you set simplify = FALSE to the sapply function both will return a list.
sapply(c(4, 9, 16), FUN = sqrt, simplify = FALSE)
as.list(sapply(c(4, 9, 16), sqrt)) # Equivalent
# return a vector with the lapply function using the unlist or simplify2array
unlist(lapply(c(4, 9, 16), sqrt)) 
simplify2array(lapply(c(4, 9, 16), sqrt)) # Equivalent

# ==========================================================================
# on certain columns
# ==========================================================================
# for all columns
df <- data.frame(x = c(6,2), y = c(3,6), z = c(2,3))
lapply(1:ncol(df), function(i) df[,i] * i)
# for certain columns
# Function applied to the first and third columns
lapply(c(1, 3), function(i) df[, i] * i)

# =========================================================================
# Nested lapply function
# =========================================================================
df <- data.frame(x = c(6,2), y = c(3,6))
# -------------------------- nested for loop ------------------------------
# Empty list
res <- vector("list", 2)
# First row by four
# Second row by four
for(i in 1:ncol(df)){
  for (j in 1:nrow(df)){
    res[[j]][i] <- df[j,i] * 4
  }
}
res
# -------------------------- nested lapply --------------------------------
lapply(1:ncol(df), function(i) {
  unlist(lapply(1:nrow(df), function(j) {
    df[j, i] * 4
  }))
})
