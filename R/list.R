# R list

# create a list include vector matrix,list
list_data<-list(c("hello","world"),matrix(c(1,2,3,4,5,6),nrow = 2),list("data","12.2"))
names(list_data)<-c("sites","numbers","lists")
print(list_data)

# access list
print(list_data[1])
print(list_data[3])
print(list_data$numbers)

# add element
list_data[4] <- "new"
print(list_data[4])
list_data["hello"] <- "x"
print(list_data)
# delete element
list_data[4]<-NULL
print(list_data[4])
# update element
list_data[3]<-"I'll replace the third element"

# merge two list
list1<-list(1,2,3)
list2<-list("It","is","sunny")
merge_list<-c(list1,list2)
print(merge_list)

# convert list to vector -> unlist
list3<-list(1:5)
print(list3)
list4<-list(10:14)
print(list4)
v1<-unlist(list3)
v2<-unlist(list4)
print(v1)
print(v2)

result = v1+v2
print(result)

# add element into the end of a column -> append()
print(list_data)
new_list <- append(list_data$numbers,0)
new_list2 <- append(1:5,0:1,after = 3)
print(new_list)
print(new_list2)

# practice
ls<-list()
for (i in 1:3) {
  j=i+1
  ls[i]=j

}
print(ls)
vls<-unlist(ls)
print(vls)

ls2<-list()
for (i in 1:3) {
  j=i+1
  ls2<-append(ls2,j)
}
print(ls2)
