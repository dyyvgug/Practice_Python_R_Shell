x = (0:100)*2*pi/100
y1 = sin(x)
y2 = cos(x)
y = cbind(y1,y2)
matplot(x,y,type = "l",lty = c(1,2))
