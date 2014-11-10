#Edgar Oliveros
#11/09/14
#InClass 10

setwd('C:/Users/Fernando/Documents/CMDA/R')

#Run the data(iris) code
data(iris)

#Examine the "names" of the variables
names(iris)

#The first 6 observations and the summaries of the variables
head(iris)
summary(iris)

#Use the sepal length and width and petal length and width features to build
#hierarchical clusters.

#features we will use to determine distances and clusters
features <- iris[,1:4]
#scale them
scaled_features <- scale(features)
#notice the new mean for each feature
summary(scaled_features)

#retain the means and std devs for each initial feature
#to be able to unscale later
#they are returned as attributes of the
#result returned by the scale() function
means <- attr(scaled_features,"scaled:center")
print(means)
stdv <- attr(scaled_features, "scaled:scale")
print(stdv)

#Distance matrix calculation
#Use Euclidean distance
distance <- dist(scaled_features, method = "euclidean")
#this matrix contains the distance between the sepal and petal length/width
print(distance)

#Create hierarchical clusters
#use the distance matrix created
hier_cl <- hclust(distance, method="ward.D")

#Plot dendogram
plot(hier_cl, labels=iris$Species)

#Separate 3 clusters and use the "Species" column from the original data to
#identify branches. They will overlap somewhat but you will still be able to see.

rect.hclust(hier_cl, k=3)
groups <- cutree(hier_cl, k = 3)
print(groups)

#What are the iris plants that seem to be mostly in first cluster? How
#about the second cluster? How about the third cluster?

#In the first cluster, they are all of type 1 (setosa) and in cluster two 
#they are all type 2(versicolor). And in the third clustert there is a mix
#type 2 and 3 (virginica)

