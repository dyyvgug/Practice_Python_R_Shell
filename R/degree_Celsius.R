#Two R functions that convert Fahrenheit temperatures to degrees Celsius and vice versa.
 
degrees.C = function(x){
  tc = (x-32)*5/9
  return(tc)
}

degrees.F = function(y){
  tf = 9*y/5+32
  return(tf)
}

oventemps.F = c(325,350,375,400,425,450)
degrees.C(oventemps.F)

oventemps.C = c(160,170,180,190,200,210,220,230)
degrees.F(oventemps.C)
 