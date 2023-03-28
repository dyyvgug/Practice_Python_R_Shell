# ===================================================================
# Draw Venn diagrams
# ==================================================================
install.packages("venneuler")
library(venneuler)
install.packages("rJava")
library(rJava)

vd <- venneuler(c(A=0.3, B=0.3, C=1.1, "A&B"=0.1, "A&C"=0.2, "B&C"=0.1 ,"A&B&C"=0.1))
plot(vd)

m <- data.frame(elements=c("1","2","2","2","3"), sets=c("A","A","B","C","C")) 
# same as c(A=1, `A&B&C`=1, C=1)
v <- venneuler(m)
plot(v)
m <- as.matrix(data.frame(A=c(1.5, 0.2, 0.4, 0, 0),
                          B=c(0  , 0.2, 0  , 1, 0),
                          C=c(0  , 0  , 0.3, 0, 1)))
# without weights
v <- venneuler(m > 0)
plot(v)
# with weights
v <- venneuler(m)
plot(v)

MyVenn <- venneuler(c(A=74344,B=33197,C=26464,D=148531,"A&B"=11797, 
                      "A&C"=9004,"B&C"=6056,"A&B&C"=2172,"A&D"=0,"A&D"=0,"B&D"=0,"C&D"=0))
MyVenn$labels <- c("A\n22","B\n7","C\n5","D\n58")
plot(MyVenn)

# customize
v$labels <- c("a","b","c")
plot(v)
