#Edgar Oliveros
#11/10/14
#InClass 11_1


library(rpart)

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

#create a new response/classification category variable
#with values 0/1 (False/True)

mtcars$response <- mtcars$am > 0
head(mtcars$response)

attach(mtcars)
##using the previously selected features (through var selection methods)
#shortcut to create formula
response
selVars = "mpg + cyl + disp + hp + drat + qsec + vs + gear + carb + gp"
f <- paste('response ~ ', paste(selVars, collapse=' + '), sep=' ')
f
tmodel <- rpart(f, data=mtcars, control=rpart.control(cp=0.01, minsplit=1, minbucket=1, maxdepth=5))
tmodel
#to visualize tree
install.packages("rpart.plot")
library(rpart.plot)
prp(tmodel)

#The decision tree shows different parameters of the motor cars and how
#their values can be used to classify the car as manual or automatic 
#transmission. These values are drat (Rear axle ratio) and disp(Displacement)

install.packages('ROCR') #only need to do this once
library(ROCR)

#using the same training data data
#should do for at least one test set as well
mtcars$pred <- predict(tmodel, newdata = mtcars)
eval <- prediction(mtcars$pred, mtcars$response) #from ROCR package

#calculate AUC

auc_calc <- performance(eval,'auc')
auc_calc@y.values #special object; this is how we extract the exact AUC part
#good AUC is close to 1; useless models have AUC of 0.5

#plot ROC curve
plot(performance(eval, "tpr", "fpr"))

fit <- rpart(mtcars$am~., data=mtcars)
fit

# make predictions (using the same training set; should also use at least one test set)
predictions <- predict(fit, mtcars, type="matrix")
# summarize accuracy
table(predictions, mtcars$am)

prp(fit)