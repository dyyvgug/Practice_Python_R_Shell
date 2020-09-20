setwd("/media/hp/disk1/DYY/R/play")
GPA.data = read.table("GPAdata.txt", header = TRUE)
GPA.data
attach(GPA.data)
univGPA
plot(ACT,univGPA,type = "p",xlab = "composite ACT",ylab = "university GPA")

univGPA.male = univGPA[sex=="m"]
ACT.male = ACT[sex=="m"]
hsGPA.male = hsGPA[sex=="m"]
housing.male = housing[sex=="m"]

GPA.data.male = data.frame(univGPA.male,ACT.male,hsGPA.male,housing.male)
GPA.data.male
write.table(GPA.data.male,file = "GPAdata_male.txt")