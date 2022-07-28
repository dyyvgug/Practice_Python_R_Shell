##ggplot2 bar plot
library(ggplot2)
library(dplyr)
library(forcats)

# count
#View(mpg)
head(mpg)
p <- ggplot() + 
  geom_bar(data = mpg, aes(x = class), stat = "count")
p

# sort bar
data_sorted <- mpg %>% 
  group_by(class) %>% 
  summarise(count = n()) %>%
  mutate(class = fct_reorder(class, count))

ggplot() + geom_bar(data =data_sorted, aes(x = class, y = count), 
                    stat = "identity")
# color
ggplot() + geom_bar(data = mpg, aes(x = class), stat = "count", 
                    fill = "white", colour="dodgerblue")

# x,y from dataframe
df <- data.frame(dose=c("D0.5", "D1", "D2"),
                 len=c(4.2, 10, 29.5))
head(df)
# Basic barplot
p<-ggplot(data=df, aes(x=dose, y=len)) +
  geom_bar(stat="identity")
p

# Horizontal bar plot
p + coord_flip()
