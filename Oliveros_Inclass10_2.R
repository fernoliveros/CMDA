#Edgar Oliveros
#11/09/14
#InClass 10_2

#Open the R file with your Inclass10_1 assignment. Rename it to
#Inclass10_12.

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
plot(hier_cl, labels=iris$Flower)

#Separate 3 clusters and use the "Species" column from the original data to
#identify branches. They will overlap somewhat but you will still be able to see.

rect.hclust(hier_cl, k=3)
groups <- cutree(hier_cl, k = 3)
print(groups)

##########################################################

#Using the iris dataset, implement the kmeans algorithm now.

#First pick number of clusters: 3

kmeans_clusters <- kmeans(distance, 3 , nstart=100, iter.max=100)

#Results of the kmeans clustering algo implementation
kmeans_clusters
kmeans_clusters$cluster
kmeans_clusters$centers

kmeans_clusters$withinss
kmeans_clusters$tot.withinss
kmeans_clusters$betweenss

kmeans_clusters$size

#Compare the two clustering algo results 
#for iris data(hier and kmeans)

compare <- cbind(groups,kmeans_clusters$cluster)
compare <- as.data.frame(compare)
names(compare) <- c("Hierarchical", "kmeans")
compare <- cbind(iris$Species,compare)
compare

#Sort data to be able to more clearly see differences between clusters
#resulting from the two algos

compare1 <- compare[order(compare$Hierarchical),]
compare1
compare2 <- compare[order(compare$kmeans),]
compare2

#how do the two algorithms fare? Are there any
#differences between the two in terms of the iris plants assignments
#to three different clusters? Are the clusters perfectly separated and
#mimicking the known Species separation?

#Both algorithms are very efficient in clustering the setosa flowers:
#Cluster 1 for Hierarchical and cluster 2 for kmeans
#For the versicolor, the Hierarchical algorithm seems to be more efficeient
#whereas the kmeans algorith places a few in different clusters. But
#overall both algorithms are efficiently separating the versicolor.

#Both alrightms have trouble separating the virginica flower.
#The Hierarchical algorithm places it in clusters 2 and 3, and the
#kmeans places it in clusters 1 and 3. Neither algorithm is efficient
#at separating the virginica flower. If I had to pick one, I would say 
#the kmeans is better, but not by much.
