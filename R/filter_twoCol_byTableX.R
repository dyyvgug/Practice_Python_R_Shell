library(dplyr)

# create example data frames
TableX <- data.frame(Column1 = c("A", "B", "C"))
TableY <- data.frame(Column1 = c("A", "B", "G","D", "E", "F"),
                     Column2 = c("1", "2", "M","A", "z", "C"),
                     Column3 = c("X", "Y", "L","Z", "W", "V"),
                     Column4 = c(11, 22, 33, 44, 55,77),
                     Column5 = c(TRUE, FALSE, TRUE, FALSE, TRUE,TRUE))

# filter out rows in TableY that do not have matching values in Column1 with TableX
result1 <- TableY %>% 
  filter(Column1 %in% TableX$Column1)
result2 <- TableY %>%
  filter(Column2 %in% TableX$Column1)

df <- rbind(result1,result2)

