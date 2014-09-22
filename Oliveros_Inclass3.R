#Edgar Olivers
#9/22/14
#Inclass3

getwd()
setwd("C://Users//Fernando//Documents//CMDA//R")

#load("exampleData.rData")
load("exampleData1.rData")
summary(custdata)
summary(medianincome)
#Merge custdata & medianincome
mergedData <- merge(custdata, medianincome)
#New variable norm.income - sacled income
mergedData$norm.income <- (mergedData$income-mergedData$Median.Income)/sd(mergedData$income)
summary(mergedData$norm.income)
# One could use this normalization to compare the cost of living and income of different
# states to aid in the decision of whether or not to move.

#2 split dat into 30% training set and 70% testing set
testSet2 <- subset(mergedData, custdata$gp <= 0.7)
trainingSet2 <- subset(mergedData, custdata$gp > 0.7)

