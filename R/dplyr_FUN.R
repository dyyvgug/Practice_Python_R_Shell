# learn dplyr package, select(),filter(),mutate(),group_by(),summarize(), setdiff()
library(dplyr) 
library(ggplot2)

head(mpg)
df <- select(mpg,model,year,cyl,cty,hwy)
df_f <- filter(df,cyl == "6")

# ==> use pipe %>% (nested)

df2 <- mpg %>%
  filter(cyl == "6") %>%
  select(model, year, cyl,cty,hwy)
# df_f is equal to df2

# unit conversions or find the ratio of values in two columns
df2 %>%
  mutate(cyl_10 = cyl*10) %>%
  head
# remove NA
df2 %>%
  mutate(cyl_10 = cyl*10) %>%
  filter(!is.na(cyl)) %>%
  head

# Split-apply-combine: split the data into groups, apply some analysis to each group, and then combine the results.
# counter
mpg %>%
  group_by(cyl) %>%
  summarise(n())

mpg %>%
  group_by(cyl) %>%
  summarise(mean_value = mean(hwy,na.rm = T))
# multiple columns
mpg %>%
  group_by(cyl,model) %>%
  summarise(min_value = min(hwy,na.rm = T))

# setdiff
df1 <- data.frame (name = c("Mike", "Paul", "Paul", "Henry"),
                   age = c(20, 21, 22, 23))
df2 <- data.frame (name = c("Sam", "Paul", "Paul", "Bob"),
                   age = c(26, 30, 22, 23))
df1_df2 <- setdiff(df1,df2)


