Fib = c(1,1,2,3,5,8,13)
Fib[3]
num.fibs = 50
seq(1,10,2)
r = numeric(num.fibs)
r[1] = 1
r[2] = 1
for (i in 2:(num.fibs-1)) {
  r[i+1] = r[i]+r[i-1]
}
r