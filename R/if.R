x = 1
if (x<2){
  y = 5
  z = 5
}else{
  y = 6
  z =6
}
  y
  z
  
  runif(10)
  
  outcomes = function(n,p){
  u = runif(n)    # generate a vector of uniform random numbers of length n.
  x = numeric(n)  # x will eventually hold the random 0's and 1's.
  for (i in 1:n) {
    if (u[i]<=p)
      x[i] = 1
    else 
      x[i] = 0
  }
    return(x)
  }
  
  n = 30
  p = .26
  num.sets = 100
  bat.ave = numeric(num.sets)
  for (i in 1:num.sets) {
    bat.ave[i] = sum(outcomes(n,p))/n    
  }
  hist(bat.ave)
  stem(bat.ave)