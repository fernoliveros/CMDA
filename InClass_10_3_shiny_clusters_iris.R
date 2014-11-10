#Shiny visualization of kmeans clusters with iris data
#use 2 features at a time to determine a variable number of clusters

data(iris)
#Examine data first
names(iris)
head(iris)
summary(iris)


#############################################
library(shiny)
runApp("App_3")

#have data loaded;
#will use the features for clustering
#and a separate variable with country names
#for labeling points in clusters
#ui and server R files should be in the folder "App_3" created
#at this location (working directory)

names(iris)
iris1 <- scale(iris[,-5])
iris1 <- as.data.frame(iris1)
names(iris1)
label_points <- iris[,5]
label_points


