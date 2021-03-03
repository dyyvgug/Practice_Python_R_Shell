# learning nested list. Yingying Dong.

x1<-c(list(1:5),list(6:10),list(11:15))

x2<-c(list(letters[1:5]),list(letters[6:10], list(letters[11:15])))
View(x2)
x3<-c(list(c("India","Australia"),list("Canada"),list(c("Russia","Malaysia"))))
x4<-c(list("Europe"),list(c("Asia","America"),list(c("Africa","Antartica"))))
x5<-c(list("Red"),list("Green"),list("Yellow"),list(c("White","Pink")))
Total_Lists<-list(x1,x2,x3,x4,x5)
View(Total_Lists)
# access the first element in each of list
lapply(Total_Lists,'[[',1)
# access the third element in each of list
el <- lapply(Total_Lists,'[[',3)
typeof(el)
