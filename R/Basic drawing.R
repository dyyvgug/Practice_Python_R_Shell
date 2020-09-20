# In the following R script,un-comment the statement corresponding to the desired graph.
#---------------------------------------------------------------------------------------
quiz.scores = c(74,61,95,87,76,83,90,80,77,91)
#hist(quiz.scores)        # histogram
#stem(quiz.scores)        # stemplot
#boxplot(quiz.scores)

# Script for a time plot.
#---------------------------------------------------------------------------------------
dry.weight = c(0.10,0.17,0.27,0.36,0.42,0.46,0.48,0.49,0.49)
time = 0 : (length(dry.weight)-1)
plot(time,dry.weight,type = "l")

#---------------------------------------------------------------------------------------

# Scatterplot example script.
# Data from the election-at-large for city council,Moscow,Idaho,1999.Seven candidates ran,
# highest number of votes got a city council seat.
# Variables are dollars spent by candidates on their campaigns,and the resulting number of 
# votes garnered.
#----------------------------------------------------------------------------------------
dollars.spent = c(0,0,404,338,583,1992,1849)
number.votes = c(159,305,706,912,1159,1228,1322)
plot(dollars.spent,number.votes,xlab = "Dollars spent",ylab = "Number of votes",type = "p")

# Side-by-side boxplot example script.
# Date from Margolese 1970 Hormones and Behavior.
# Androsterone levels (mg in 24 hr in urine sample) and sexual orientation 
# (S : straight, G : gay)in 26 human males.
#-----------------------------------------------------------------------------------------
level.andro = c(3.9,4.0,3.8,3.9,2.9,3.2,4.6,4.3,3.1,2.7,2.3,2.5,1.6,3.9,3.4,2.3,1.6,2.5,
                3.4,1.6,4.3,2.0,1.8,2.2,3.1,1.3)
length(level.andro)
orientation = c("S","S","S","S","S","S","S","S","S","S","S","G","G","G","G","G","G","G","G",
                "G","G","G","G","G","G","G")
boxplot(level.andro~orientation,range = 0,names = c("Gay","Straight"),boxwex = .5,
        ylab = "Androsterone_level")

# Bar graph example script.
# Percent of young voters,ages 18-29,voting
# Democratic in US presidential elections,1992-2008.Source:Pew Research.
Young.percent = c(43,53,48,54,66)
barplot(Young.percent,xlim = c(0,1),width = .05,ylim = c(0,70),names.arg = c("1992","1996",
"2000","2004","2008"),space = 1)
