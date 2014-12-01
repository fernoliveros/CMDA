# Edgar Oliveros
# InClass 12
# 12/01/14


setwd('C:/Users/Fernando/Documents/CMDA/R')
load('KDD2009.Rdata') #same KDDcup data
library(ROCR)
library(rpart)
library(class)

#Use mtcarsin data for KDD Cup
#use pre-selected 27 variables as features
#previous data wrangling and variable selection 

names(mtcars)
#use Churn as the outcome
head(mtcars$churn) # 1 and -1 type variable; 1 is pos outcome

#create the 0/1 response/class variable
mtcars$response <- mtcars$churn > 0

#svm for classification into two classes based on features#####################
install.packages('kernlab')
?ksvm
library(kernlab)
system.time(mSVMV <- ksvm(as.formula(f),data = mtcars, kernel = 'vanilladot')) #bad kernel function

f <- paste('response ~ ',paste(selVars,collapse=' + '),sep='')
f

#predict
svm_pred <- predict(mSVMV, newdata = mtcarsin, type = 'response')
head(svm_pred)
#calculate AUC for SVM
#notice that second column from predictions denotes "p of pos"
eval <- prediction(svm_pred, mtcarsin$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values

#next, good kernel function, commonly used#####################################

system.time(mSVMV1 <- ksvm(as.formula(f),data = mtcarsin, kernel = 'rbfdot')) 

#predict
svm_pred1 <- predict(mSVMV1, newdata = mtcarsin, type = 'response')
head(svm_pred1)
#calculate AUC for SVM
#notice that second column from predictions denotes "p of pos"
eval <- prediction(svm_pred1, mtcarsin$response) 
auc_calc <- performance(eval,'auc')
auc_calc@y.values
