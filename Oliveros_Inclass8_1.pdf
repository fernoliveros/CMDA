#Edgar Oliveros
#InClass 8_1
#10/27/14


#1. Create a new ipython notebook Inclass8_1.ipynb.
#2. Install the pyper library.
#3. Import the necessary libraries: pandas, pyper, matplotlib.
import pandas as pd
import pyper as py
import matplotlib as mpl

#4. Read in the Iris data (csv file on Scholar/Resources/Data) as a pandas DataFrame.
iris = pd.read_csv('iris.csv')

#5. Examine the data and get numerical summaries using pandas capabilities: .head(), .shape, 
#.describe, value_counts.
iris.head()
iris.shape
iris.describe

#6. Create an R instance with pyper. Be sure to include the full path to your R installation.
r = py.R(RCMD = 'C:\\Users\\Fernando\\R\\bin\R', use_pandas = True)

#7. Pass data from Python to R.
r.assign("rdata", iris)

#8. Now use the “rdata” and R capabilities to: examine the data (head() function, names() function), 
#get numerical summaries (correctly, depending on if a variable is numeric or factor)
print r("head(rdata)")
print r("names(rdata)")
print r("summary(rdata)")

#9. Access the help file for the R’s princomp function
r("?princomp")

#10. Calculate the principal components of the iris data and assign the result to an R object that you 
#can name “p”
r("p = princomp(rdata)")

#11. Display the “names” in the object “p”
print r("names(p)")

# 12. The actual principal components are saved in the “scores” name in the object “p”. All the 
# principal components are calculated by default (as many as the number of columns in the data 
# set used to calculate the principal components). Display the first 6 rows of the principal 
# components. 
print r("head(p$scores, n=6")

# 13. Now pass the principal components you have just visualized into a pandas data frame. Be sure 
# to give proper names to columns using the pd.DataFrame’s argument “columns”.
irisPDF = pd.DataFrame(r.get("p$scores"),columns=['pc1','pc2','pc3','pc4','pc5'])

#14. Examine the newly created pandas dataframe with .head().
irisPDF.head()

#15. Now create a basic scatterplot of the first two principal components (with matplotlib.pyplot 
#capabilities). Is there a pattern in the data?
mat.scatter(irisPY.Comp1,irisPY.Comp2).
title('iris').
xlabel('PC 1').
ylabel('PC 2')
mat.show()
	  
# Next use the example code from last lecture and build the scatterplot for the first two principal 
# components with the three species differentiated by color. You will have to figure to modify the 
# code slightly to assign different colors to the different species and to display the correct legend. 
# What patterns do you observe now? Are the first two principal components good at 
# summarizing the info in the dataset and discriminating between the three species?
colors = ['blue', 'yellow', 'red']
labels = ['Setosa', 'Virginica', 'Versicolor']

fig = mat.figure()
leg = mat.add_subplot(1, 1, 1)

leg.set_xlabel('PC 1')
leg.set_ylabel('PC 2')

for a in xrange (len(colors)):
    x = irisPDF.Comp1[:][iris.Species == a]
    y = irisPDF.Comp2[:][iris.Species == a]
    plt.scatter(x, y, c = colors[a], label = labels[a])
mat.show()

# The first two principal components are sufficient for summarizing 
#the info in the dataset and discriminating betweenthe three species