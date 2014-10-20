# Edgar Oliveros
# InClass 7
# CMDA 3654
# 10/20/14

#1) Create a new ipython notebook.

import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as mpl

#2) Use the data for your project as a panda dataframe.

cfoot = pd.read_csv('cfb2013stats.csv', header = True)

#3) For suitable variables, plot : 
#1. a histogram;

hist = cfoot.hist(bins = 30)
mpl.title("Histogram")
hist.get_figure().savefig("hist.png")

#2. a density plot;
dens = cfood.plot(kind 'kde')
mpl.title("Density Plot")
dens.get_figure().savefig("dens.png")

#3. a bar chart; 
r1 = cfoot[cfoot['ScoreOff'] == 4]
bar = r1.plot(kind = 'bar')
mpl.title("Bar Graph")
bar.get_figure().savefig("bar.png")

#4. a horizontal stacked bar chart with categories summing to 1;
stak = cfoot.plot(kind = 'barh', stacked = True)
mpl.title("Stacked Bar plot")
stak.get_figure().savefig("stak.png")

#5. a scatterplot.
scat = mpl.scatter(cfoot, r1)
mpl.title("Scatter Plot")
scat.get_figure().savefig("scat.png")

#4) Save all figures as png in your working directory. Submit the pngs with your in 
#class assignment.

#---------------------------------------------------------------

#1. Create a new ipython notebook Inclass7_2.ipynb.

import scipy as sp
import sklearn as sk
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as mpl

#2. Download Medical.csv from scholar/Data and import it as a pandas dataframe. You will 
#train a linear classifier to separate diabetic subjects (all subjects included in the dataset 
#are diabetic) into two classes of health literacy (how much they know about health) based 
#on their age and measured average blood glucose.

med = pd.read_csv('Medical.csv')

#3. Wrangle your data with pandas. Keep features “age” and “HgA1c”. Create target variable 
#literacy with levels 0=“low literacy” and 1= “high literacy” based on the dataframe’s
#variable “literacy” with levels “low” and “high”.

med.replace(to_replace='HIGH',value=1, inplace=True)
med.replace(to_replace='LOW',value=0, inplace=True)

#4. Setup the numpy arrays X and y.

X = np.array(med[['Age', 'HgA1C']])
y = np.array(med['A Literacy Category'])


#5. Take a 75% training set and a 25% testing set using the scikit-learn capabilities.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

#6. Scale your features.

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#7. Train the classifier. Write out the classifier’s equation.

clf = SGDClassifier()
clf.fit(X_train, y_train)

#8. What is the classifier’s accuracy on the training data?

y_train_prediction = clf.predict(X_train)
metrics.accuracy_score(y_train, y_train_prediction)
#91.9%.

#9. What is the classifier’s accuracy on the test set?

y_test_predict = clf.predict(X_test)
metrics.accuracy_score(y_test, y_test_predict)
#92.3%

#10. What is the confusion matrix and what is the interpretation of each number in the 
#matrix?

metrics.confusion_matrix(y_train, y_test_predict)
# array([[0,  4], [ 0,  33]])
#incorrectly predicted low 0 and high 4 times.
metrics.confusion_matrix(y_test, y_test_predict)
# array([[13]])
#predicted 13 results correctly

#11. Comment on the quality of this classifier for this problem.
#Although the accuracy is above 90% and it did predict all 13 results correctly
#I would still say that this classifier is not very good. To be able
#to accurately tell how good this classifier is we would need a bigger
#dataset. Also plots of the test data show that there are no low litteracy
#scores.

#------------------------------------------------------------

#1) Download the PCA notebook from Scholar 
#Resources/Assignments.

import numpy as np
import scipy as sp
import sklearn as sk
import pandas as pd
import matplotlib.pyplot as mpl

#import and load 
from sklearn.datasets import load_digits
digits = load_digits()

#Show names
print digits.keys()
digits.target_names
X_digits, y_digits = digits.data, digits.target

#X matrix
X_digits.shape

# Import PCA.
from sklearn.decomposition import PCA
estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)

#PCA matrix 
X_pca.shape
X_pca

#2) Run the code to get the principal components, and create the 
#scatterplot. Comment on what digits are easiest to separate 
#and which one might be easily confounded, using only the 
#information carried in the first two principal components.

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 0][y_digits == i]
    py = X_pca[:, 1][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

#3) Modify the scatterplot code to visualize the last two principal 
#components (8 and 9). Change the axes labels accordingly.

colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in xrange(len(colors)):
    px = X_pca[:, 8][y_digits == i]
    py = X_pca[:, 9][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('Ninth Principal Component')
plt.ylabel('Tenth Principal Component')

#4) Comment on the ability of this new visualization to distinguish 
#between images of digits. 

# This new visualizations is not adequate to distinguish between
# images. The data is very crowded and not very well separated 
# therefore making it difficult to identify digits.
