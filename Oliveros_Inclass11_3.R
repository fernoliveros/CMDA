#Edgar Oliveros
#11/16/14
#InClass 11_2

#Load data
data(mtcars)
#Examine
head(mtcars)
names(mtcars)

?mtcars
#mpg = miles per galon
#cyl = number of Cylinders
#disp = Displacement (cu.in.)
#hp = Gross horsepower
#drat = Rear axle ratio
#wt = Weight (lb/1000)
#qsec = 1/4 mile time
#vs = V/S
#am = Transmission(0 = automatic, 1 = manual)
#gear = Number of forward gears
#carb = Number of carburetors

library(ROCR)
library(rpart)
library(class)


# create random variable and extract a 50% training and 50% test set
mtcars$rv <- runif(dim(mtcars)[1])
train <- subset(mtcars, mtcars$rv > 0.25)
test <- subset(mtcars, mtcars$rv <= 0.25)

head(train$am)  
head(test$am)   

# create the response variable in the training set
train$response <-train$am > 0
head(train$response)

################# KNN
system.time(knnDecision <- knn(knnTrain,knnTrain,response,k=20,prob=T))
?knn#to learn more about the knn implementation

#the values of knnDecision are classifications
head(knnDecision)

#the "prob" argument returns, for each observation, the proportion of
#votes for the winning class (pos or neg)
#we want the predicted probabilities (which is p = probability(pos))
#so we will use the "prob" attribute values
#to get the p predictions


knnPred <- ifelse(knnDecision==TRUE,
                  attributes(knnDecision)$prob,
                  1-(attributes(knnDecision)$prob))
head(knnPred)

#calculate AUC
library(ROCR)
eval <- prediction(knnPred, response) #from ROCR package
auc_calc <- performance(eval,'auc')
auc_calc@y.values #special object; this is how we extract the exact AUC

# AUC = 77.0%

#################Logistic algo

#compare to logistic regression AUC and system time
f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='') #create formula
system.time(gmodel <- glm(as.formula(f),
                          data=knnTrain,
                          family=binomial(link='logit'))) #get system time and train the model
log_predict <- predict(gmodel, 
                       newdata=knnTrain, 
                       type = "response") #get p predictions

#get AUC for logistic model

eval <- prediction(log_predict, response) #from ROCR package
auc_calc <- performance(eval,'auc')
auc_calc@y.values #special object; this is how we extract the exact AUC part

#AUC 80%

###########CART algo
#train CART decision tree, get AUC and system time
library(rpart)
f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')
system.time(tmodel <- rpart(f,data=mtcars,
                            control=rpart.control(cp=0.001,minsplit=1000,
                                                  minbucket=1000,maxdepth=5)))

mtcars$pred <- predict(tmodel, newdata = mtcars)
mtcars$response <- mtcars$am > 0

#calculate AUC for CART decision tree
eval <- prediction(mtcars$pred, mtcars$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

############### Naive Bayes

#Package for Naive Bayes implementation
install.packages("e1071")
library(e1071)

#train model on selected variables from mtcars data set
#use the shortcut to formula as before

#train the model
system.time(fit <- naiveBayes(as.formula(f), data=train))

#make predictions
system.time(naivB_pred <- predict(fit, dTrain, type = 'raw'))
head(naivB_pred) #need just the "probability of TRUE" as prediction

?naiveBayes

#calculate AUC for Naive Bayes
#notice that second column from predictions denotes "p of pos"
eval <- prediction(naivB_pred[,2], dTrain$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

#AUC = 99%

#Naive Bayes is the most accurate and the least efficient. The time 
# elapsed is the primary factor in algorithm accuracy. The more time
# elapsed, the more accurate
