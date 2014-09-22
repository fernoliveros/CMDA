#Edgar Oliveros
#09/22/14
#Homework 3

getwd()
setwd("C:\\Users\\Fernando\\Documents\\CMDA\\R")

myData<- read.table("cfb2013stats.csv", sep=",", header=TRUE)

summary(myData)
summary(myData$ScoreOff) #No issue
summary(myData$RushAttOff) #No issue
summary(myData$RushYdsOff) #Min is negative
summary(myData$PassAttOff) #No issue
summary(myData$PassCompOff)#No issue
summary(myData$PassYdsOff)#No issue
summary(myData$PassIntOff)#No issue but should use integers
summary(myData$FumblesOff)#Negative Min
summary(myData$Opponent)#No issue
summary(myData$ScoreDef)#No issue
summary(myData$RushAttDef)#No issue
summary(myData$PassAttDef)#No issue
summary(myData$PassCompDef)#No issue
summary(myData$PassYdsDef)#Negative Min
summary(myData$PassIntDef)#Integers
summary(myData$FumblesDef)#Use integers
summary(myData$Site)#No issue
summary(myData$Line)#Many NA's

plot(myData$PassAttOff, myData$PassCompOff)#In this plot you can see the
#direct relationship between pass attempts and pass completions. 

hist(myData$ScoreOff, breaks = 15)
plot(density(myData$ScoreOff))
#Above are a histogram and density plot of the score of offense which you can see
#is a normal curve that is slightly right skewed with a mean of around 30

boxplot(myData$ScoreDef)
#this plot shows a box plot of the score on def and as you can see there are a 
#few outliers that must be the teams with the best defense