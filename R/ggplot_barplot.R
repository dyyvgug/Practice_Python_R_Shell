##ggplot2 bar plot
library(ggplot2)
library(dplyr)
library(forcats)
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


