if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("tidyverse")
BiocManager::install("hrbrthemes")
BiocManager::install("babynames")
BiocManager::install("viridis")
library(tidyverse)
library(hrbrthemes)
library(babynames) # it's a baby name data. year,sex,name,n,prop
library(viridis)

# Load dataset from github
data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/3_TwoNumOrdered.csv", header=T)
data$date <- as.Date(data$date)

don <- babynames %>% 
  filter(name %in% c("Ashley", "Amanda", "Mary", "Deborah",   "Dorothy", "Betty", "Helen", "Jennifer", "Shirley")) %>%
  filter(sex=="F")

# Plot
don %>%
  ggplot( aes(x=year, y=n, group=name, fill=name)) +
  geom_area() +
  scale_fill_viridis(discrete = TRUE) +
  theme(legend.position="none") +
  ggtitle("Popularity of names in the previous 30 years") +
  theme_ipsum() +
  theme(
    legend.position="none",
    panel.spacing = unit(0, "lines"),
    strip.text.x = element_text(size = 8),
    plot.title = element_text(size=13)
  ) +
  facet_wrap(~name, scale="free_y")
#scale="free_y": This part of the code specifies 
#that you want the y-axis scales to be "free" or 
#independent for each facet. This means that the 
#y-axis range (the minimum and maximum values) can 
#vary between facets based on the data within each facet. 
#This is particularly useful when the data in different 
#facets have different ranges, and you want to 
#avoid distorting the visual representation by 
#forcing a common y-axis scale.