#1
getwd()
setwd("C:\\Users\\Fernando\\Documents\\CMDA\\R")

#The health insurance customer data
load('exampleData.rData')
#Examine data
names(custdata)
dim(custdata)
class(custdata)

#Summary statistics

summary(custdata) #for the entire data frame

#look at individual variables to spot problems

summary(custdata$is.employed)
#There are 328 NA's when it should be clear wether someone is employed or not
summary(custdata$income)
#The min value is negative which may mean the person is in debt or it is a mistake
summary(custdata$age)
#the max age is 146.7 years which is not realistic



#2
uciCar <- read.table(
  'http://www.win-vector.com/dfiles/car.data.csv',
  sep=',',
  header=T)
summary(uciCar$buying)
#The high low med and vhigh values are all the same which is odd
summary(uciCar$maint)
#Again the high low med and vhigh values are all the same 
summary(uciCar$doors)
#Same values as before and headers are numbers one of which is "5more"
summary(uciCar$persons)
#The headers are numerical values one of which is more, furthermore they 
#have the same values
summary(uciCar$lug_boot)
#Again, these have the same value. This time 576
summary(uciCar$safety)
#Once again as the summary for lug_boot these all have the value 576
summary(uciCar$rating)
#This set actually seems to be better except for maybe the value of unacc being
#too high (1210) 

#3
load('credit.Rdata') #From lecture 6
save(d, file ="credit.RData")
summary(d$Personal.status.and.sex)
#There are no single females! The total amount of females and males are not
#very close. Furthermore there are many more single men whereas all females
# are divorced, separated, or married
summary(d$Other.debtors)
#About 90% of the elements are "none" the rest are co-applicants and guarantors

############# PART II ###############
install.packages("hexbin")
install.packages("ggplot2", dependencies=TRUE) 
library("hexbin")
library(ggplot2)
custdata2 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0 & custdata$income < 200000))
hexbinplot(income ~ age, custdata2)
ggplot(custdata2, aes(x=age,y=income)) +
  geom_point() +
  ylim(0,200000) +
  theme_bw() +
  ggtitle("Age vs Income")
#Collection data points are easier to pick out, however it is similar to the scatterplot

hexbinplot(num.vehicles ~ income, custdata)
#Higher income people seem to have more vehicles however it is not very clear

ggplot(custdata) + geom_bar(aes(x=recent.move,
                                fill=income.lt.30K),
                            position="fill") +
  theme_bw()+
  ggtitle("Recently Moved vs. 30k or less Income")
#There are more people moving with incomes < 30k as shown by this bar graph