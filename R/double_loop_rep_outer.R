# Double loop
# a=j+10i,ask the matrix of a; i=1:4,j=1:30

#method 1
i = 1:4
j = 1:30
ni = length(i)
nj = length(j)
a <- matrix(NA,ni,nj) #initiate a matrix with nj rows and ni columns
for (x in 1:ni) {
  for (y in 1:nj) {
    a[x,y] = i[x]*10 + j[y]
  }
}
print(a)
#method2
a<-matrix(rep(i,each=nj)*10+rep(j,ni),nj,ni)
print(a)
#method3
a<-outer(1:4,1:30,function(x,y) 10*x + y)
print(a)
