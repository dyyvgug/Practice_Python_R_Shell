2*(1.008)+1*(16.00)

molar.mass=function(x,y){
  mm=sum(x*y)
  return(mm)
}

num.atoms=c(2,1)
atomic.weights=c(1.008,16.00)
molar.mass(num.atoms,atomic.weights)

num.atoms=c(12,22,11)
atomic.weights=c(12.01,1.008,16.00)
molar.mass(num.atoms,atomic.weights)

