#
# Final project - visilusations
#

import pandas
import numpy
from pyper import *

r = R()

def run():
    r('''
cfb <- read.csv("data/cfb2013stats.csv")

library(rpart)
library(ROCR)

summary(cfb)

# TRUE / FALSE if the offensive team has won.
cfb$response <- (cfb$ScoreOff - cfb$ScoreDef > 0)
summary(cfb$response)

train <- subset(cfb, cfb$ScoreOff > 0.1)
test <- subset(cfb, cfb$ScoreOff <= 0.1)

selVars <- "TeamName + ScoreOff"
f <- paste('response ~ ', paste(selVars, collapse=' + '), sep='')

tmodel <- rpart(
    f,
    data=train,
    control=rpart.control(
        cp=0.001,
        minsplit=10,
        minbucket=10,
        maxdepth=5))

train$pred <- predict(tmodel, newdata = train)


eval_cart <- prediction(train$pred, train$response) 
auc_calc <- performance(eval_cart, 'auc')

auc_calc@y.values
''')

run()
