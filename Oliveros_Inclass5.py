#Edgar Oliveros
#10/06/14
#CMDA 3654
#Inclass Assignment 5


#PART 1
#1. Run iPython


#2. Import modules pandas, numpy and matplotlib
#Find out what functions each of them implement with the help of Tab Completion functionality. 
import pandas
import numpy
import matplotlib
#run: "pandas.<TAB>" to see pandas functions and the same for the other modules


#3. Select 5 commands from these modules. Find a way to look for these function using ? and 
#wildcards.

pandas.cut?
pandas.Spar*?
np.in*?
np.fv?
matplotlib.afm?


#4. Use all the short-cut commands.
# Ctrl+L clears the screen
# Use up and down arrows to scroll through commands and results
# i_# (# being the command line number) displays the input on line #
# _# displays the output on line #

#5. Run all the magic commands.
%reset
#Deletes all objects and variables 

%run
#Runs the file named

%paste
#Pastes copied text

%quickref
%Goes to iPython Quick Reference Card

%timeit
#Computes average execution time for certain piece of code

%hist
#Displays input history

%pwd
#Returns current working directory

%cd directory_name
#changes working directory to the named one

%ls
#see all files in current working directory


#6. Use your Inclass4_3, Part I and run snippets of code in iPython by copy-paste.
#copied and pasted cities but for sake of assignment I will set it below
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
#then called cities to make sure it worked
cities


#7. Introspect magic command %xdel, function str.split, module re and matplotlib.pylab.

%xdel?
#Type- Magic function
#Delete a variable, trying to clear it from anywhere that IPython's machinery
#has references to it. By default, this uses the identity of the named object 
#in the namespace to remove references held under other names. The object is also
#removed from the output history

str.split?
#Return a list of the words in the stringS, using sep as the
#delimiter string. If maxsplit is given, at most maxsplit
#splits are done. If sept is not specified or is None, any
#whitespace string is a separator and empty string are removed 
#from the results

import re
re?
#Provides regular expression matching operation similar to those 
#found in Perl. It looks for pattern to identify matches, substitute, 
#and make splits

import matplotlib.pylab
mayplotlib.pylab?
#This is a procedural interface to the matplotlib object-oriented
#plotting library.


#8. Start pylab; build the plot on slide 10; do tab completion on numpy.;do introspection on 
#numpy.random; find the line about randn. What type of numbers does it generate?

import numpy
a = numpy.random.randn(100)
plot(a.cumsum())
numpy.random?
numpy.random.randn?
# random generates random numbers and randn generates normally distributed values.

#9. Find out what cumsum does.

numpy.cumsum?
#Returns the cummulative sum of the elements along a given axis.


#10. How long does it take to generate 100 normally distributed random numbers? How about 
#1000? How about 10,000?How did you find that out?(hint: run magic command timeit)

%timeit numpy.random.randn(100)
%timeit numpy.random.randn(1000)
%timeit numpy.random.randn(10000)
#7.16 micro seconds per loop for 100000 loops
#59.9 micro seconds per loop for 10000 loops
#591 micro seconds per loop for 1000 loops

#------------------------------------------------------------
#PART 2

#1) Create a new ipython notebook “Inclass5_2”

import numpy as np

#2) Create two one-dimensional arrays with 5 elements of your choice. Display arrays’ shape and type.


array1 = np.array([1,2,3,4,5])
array2 = np.array([5,4,3,2,1])
np.shape(array1)
np.shape(array2)
array1.dtype
array2.dtype

#3) Do element-wise summation for the two arrays. 

array1 + array2

#4) Do element-wise product for the two arrays.

array1 * array2

#5) Create a 6X6 identity matrix.

idenM = np.matrix(np.identity(6))


#6) Replace all element on third row with value 5.

idenM[2,] = 5

#7) Replace all elements that are not zero with value 6 using a boolean indexing and slicing.

idenM[idenM != 0] = 6


#8) Create an empty 3 dimensional array, arr3 with shape (2,3,4), and elements of integer type. 

array3 = np.empty((2,3,4), dtype = int)


#9) Display its number of dimensions, shape and type of each element. 

array3.ndim
array3.shape
array3.dtype


#10) Give the second element on the third dimension, from the second group on the second dimension,
# from the first group on the first dimension the value 5.

array3[0,1,1] = 5

#11) Generate an array of 20 uniformly distributed random numbers with values between 0 and 1.

array4 = numpy.random.random_sample(20)

#12) Get the min, max, sum, mean, and standard deviation of the array in part 11.

np.min(array4)
np.max(array4)
np.sum(array4)
np.mean(array4)
np.std(array4)

#13) Replace all elements less than 0.5 with 0 and all elements larger than 0.5 with 1 in the array 
#from part 11 using “where” function.

np.where(array4 < 0.5, 0, 1)

#14) Sort the array in part 11.

array4.sort()

#15) Find the unique values in the same array.

np.unique(array4)

#------------------------------------------------------------------------
#PART 3


#1) Go to quandl.com. Open an account. Go to the “Account Settings” and make note of your API 
#Key.

 Account key: 9TJu7joGAcvs5N-y_ghg

#2) Go to https://github.com/quandl/Python. Click on “Download ZIP”. Unzip folder and copy 
#“setup.py” and “Quandl” folders into your local folder where you run ipython. (EG: 
#C:\Users\Denisa)

#done

#3) Create a new ipython notebook, In5_3. Import pandas module. Import Quandl module by 
#“import Quandl”. Since we already have the required NumPy and Pandas modules, it should 
#work for you.

import pandas
import Quandl

#4) Go to https://www.quandl.com/c/markets/bitcoin-data

#k

#5) You will import data for Bitcoin exchange rates to USD on different venues: Bitstamp, Bitfinex 
#and LakeBTC. Go to:
#https://www.quandl.com/BCHARTS/BITSTAMPUSD
#Click on “Python” Library on the right. The code you need to use to import data will show up.
#Import only 2014 data to September30. Use your authentication key. Example code:
#bitstamp = Quandl.get("BITCOIN/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-
#30", authtoken="2_mykey_T")
#Import in separate DataFrames the data for Bitfinex and LakeBTC as well. 


BitStamp = pandas.DataFrame(Quandl.get("BCHARTS/BITSTAMPUSD", 
	trim_start="2011-09-13", 
	trim_end="2014-10-02", 
	authtoken="izgPWeFG7v_PXzz2wtr9"))

BitFinex = pandas.DataFrame(Quandl.get("BCHARTS/BITFINEXUSD",
    trim_start="2013-03-31", 
    trim_end="2014-10-02", 
    authtoken="izgPWeFG7v_PXzz2wtr9"))

LakeBTC = pandas.DataFrame(Quandl.get("BCHARTS/LAKEUSD", 
	trim_start="2014-03-01", 
	trim_end="2014-10-02", 
	authtoken="izgPWeFG7v_PXzz2wtr9"))


#6) View your three created pandas data frames using df_name.head(). What are the column 
#names? What is the frequency of data (daily/weekly/yearly Bitcoin prices)? Answer in comments

BitStamp.head()
BitFinex.head()
LakeBTC.head()


#7) Create three objects ind1, ind2, and ind3 containing the index of each of the created 
#dataframes.

ind1 = BitStamp.index
ind2 = BitFinex.index
ind3 = LakeBTC.index


#8) Display ind1, ind2, ind3. How many elements are in each?

ind1
#1116 elements
ind2
#551 elements
ind3
#216 elements

#9) Display the .values attribute of each of ind1, ind2, ind3. What type of object is being displayed 
#for each? What dtype is each element of the displayed object? Answer with comments.

ind1.values
ind2.values
ind3.values
#They display array of strings

#10) Display the .columns attribute of each DataFrame. How many columns do we have in each?

BitStamp.columns
BitFinex.columns
LakeBTC.columns
#7 columns in each

#11) Drop the variable showing BTC volume from each dataframe using the .drop method.

BitStamp.drop(['Volume (BTC)'], 1)
BitFinex.drop(['Volume (BTC)'], 1)
LakeBTC.drop(['Volume (BTC)'], 1)



