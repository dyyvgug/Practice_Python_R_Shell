a <- matrix(1:9, nrow=3) 
a
threshhold <- 8  
subset(a, a[ , 2] < threshhold) 
