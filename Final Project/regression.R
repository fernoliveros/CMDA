setwd("C:\\Users\\Kyle\\Dropbox\\CS\\CS3654\\Final Project")
cfb <- read.csv("data/cfb2013stats.csv")

library(rpart)
library(ROCR)

summary(cfb)

# TRUE / FALSE if the offensive team has won.
cfb$win <- (cfb$ScoreOff - cfb$ScoreDef)
summary(cfb$response)

train <- subset(cfb, cfb$ScoreOff > 14)
test <- subset(cfb, cfb$ScoreOff <= 14)
attach(train)

# Fit linear regression with all features
fit <- lm(win ~ RushAttOff + RushYdsOff + PassAttOff + PassCompOff + PassYdsOff + PassIntOff + FumblesOff +  
            RushAttDef + RushYdsDef + PassAttDef + PassCompDef + PassYdsDef + PassIntDef + FumblesDef + Site)

summary(fit)
step <- stepAIC(fit, direction = "both")
step
step$anova

rm(step)
rm(fit)

# Build model with only retained variables
fit1 <- lm(win ~ RushYdsOff + PassAttOff + PassCompOff + PassYdsOff + PassIntOff + FumblesOff +  
            RushAttDef + RushYdsDef + PassAttDef + PassCompDef + PassYdsDef + PassIntDef + FumblesDef)

summary(fit1)

# Remove training set (no longer needed)
detach(train)
rm(train)

# Now predict using the test set
test$win_pred <- predict(fit1, newdata = test)

rm(fit1)

#See how predicted ssc compares to actual ssc values
library(ggplot2)
ggplot(data = test, aes(x = win_pred, y = win)) +
  geom_point(color = "red") +
  geom_line(aes(x = win, y = win), color = "blue")

