library(ggplot2)
head(mpg)
View(mpg)
ggplot(mpg,aes(x=class)) + geom_bar()
ggplot(mpg,aes(x=class,y=displ)) + geom_bar(stat="identity")
ggplot(mpg,aes(x=class)) + geom_bar(aes(weight=displ))

ggplot(mpg,aes(x=class)) + geom_bar(fill=1:7)
ggplot(mpg,aes(x=class)) + geom_bar(aes(fill=factor(cyl)))
ggplot(mpg,aes(x=class)) + geom_bar(aes(fill=factor(displ)))
ggplot(mpg,aes(x=class)) + geom_bar(aes(color=factor(cyl)))

##Group bar chart, three presentation forms
ggplot(mpg,aes(x=class)) + geom_bar(aes(fill=factor(cyl)),position="stack") #default
ggplot(mpg,aes(x=class)) + geom_bar(aes(fill=factor(cyl)),position="dodge") #parallel
ggplot(mpg,aes(x=class)) + geom_bar(aes(fill=factor(cyl)),position="fill") # fill display scale

ggplot(mpg,aes(x=class)) + geom_bar() + coord_flip() #landscape

ggplot(mpg, aes(class))+geom_bar()+coord_polar(theta = "y")
ggplot(mpg, aes(class))+geom_bar()+coord_polar(theta = "x")
ggplot(mpg, aes(class))+geom_bar(aes(fill=factor(displ)))+coord_polar(theta = "y")
ggplot(mpg, aes(class))+geom_bar(aes(fill=fl))+coord_polar(theta = "x")
