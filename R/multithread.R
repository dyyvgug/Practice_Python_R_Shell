# ================================================
# Yingying Dong. Learn multithreading in R
# ================================================
library(parallel)
library(MASS)

x <- iris[which(iris[,5]!="setosa"),c(1,5)]
trials <- 10000
res <- data.frame()
system.time(
  {
    trial <- 1
    while (trial <= trials) {
      ind <- sample(100,100,replace = T)
      result1 <- glm(x[ind,2]~x[ind,1],family = binomial(logit))
      r <- coefficients(result1)
      res <- rbind(res,r)
      trial <- trial + 1
    }
  }
)
# ====================================================
# Use lapply()
# ====================================================
trials <- seq(1,10000)
boot_fx <- function(trial){
  ind <- sample(100,100,replace = T)
  result1 <- glm(x[ind,2]~x[ind,1],family = binomial(logit))
  r <- coefficients(result1)
  res <- rbind(data.frame(),r)
}
system.time({
  results <- lapply(trials,boot_fx)
})
# ===================================================
# Parallelization
# ===================================================
starts <- rep(100,40)
#print(starts)
fx <- function(nstart) kmeans(Boston,4,nstart = nstart)
system.time(
  results <- lapply(starts, fx)
)
system.time(
  results <- mclapply(starts,fx,mc.cores = 8)
)

x <- iris[which(iris[,5] != "setosa"), c(1,5)]
trials <- seq(1, 10000)
boot_fx <- function(trial) {
  ind <- sample(100, 100, replace=TRUE)
  result1 <- glm(x[ind,2]~x[ind,1], family=binomial(logit))
  r <- coefficients(result1)
  res <- rbind(data.frame(), r)
}
system.time(
  {
    results <- mclapply(trials,boot_fx,mc.cores = 8)
  }
)
# ======================================================
# foreach and doParallel
# ======================================================
for (i in 1:3) {
  print(sqrt(i))
}
library(foreach)
foreach(i=1:3) %do%{
  sqrt(i)
}
library(doParallel)
registerDoParallel(numCores)  # use multicore, set to the number of our cores
# To simplify output, foreach has the .combine parameter that can simplify return values
# Return a vector
foreach (i=1:3) %dopar% {
  sqrt(i)
}
# Return a data frame
foreach (i=1:3, .combine=c) %dopar% {
  sqrt(i)
}
# Let's use the iris data set to do a parallel bootstrap
# From the doParallel vignette, but slightly modified
x <- iris[which(iris[,5] != "setosa"), c(1,5)]
trials <- 10000
system.time({
  r <- foreach(icount(trials), .combine=rbind) %dopar% {
    ind <- sample(100, 100, replace=TRUE)
    result1 <- glm(x[ind,2]~x[ind,1], family=binomial(logit))
    coefficients(result1)
  }
})
# And compare that to what it takes to do the same analysis in serial
system.time({
  r <- foreach(icount(trials), .combine=rbind) %do% {
    ind <- sample(100, 100, replace=TRUE)
    result1 <- glm(x[ind,2]~x[ind,1], family=binomial(logit))
    coefficients(result1)
  }
})
stopImplicitCluster()
