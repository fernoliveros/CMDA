#Edgar Oliver
#Inclass Assignment 6
#10/06/14

#PART I: 6_1
#1 & 2) done
import pandas as pd

#3)
#import work_tab
workTab = pd.readtable('work_tab.txt')
workTab

#import work_comma
workComma = pd.read_csv('work_comma.csv', sep = ',')
workComma

#import stress2_1 with only last two observations 
stress = pd.read_table('stress2_1.txt', skiprows = 19)
stress

#use githup API to create a pandas data frame with 4 cols 
r = request.get('https://api.github.com/')
rj = r.json()
fields = ['col1', 'col2', 'col3','col4']
df = pd.DataFrame(rj, fields)
df

#Save as pickle
df.to_picle('dfPickle')

#Load pickle
pd.read_pickle('dfPicke')

#Save in HDF5 format
frameStore = pd.HDFStore('githubFrame.h5')
frameStore['arg1'] = df

#Access it
frameStore['arg1']

################################################
#Part II: 6_2

import pandas as pd
import numpy as np
import math

#1) Import your project data using one of the read_csv or read_table methods for 
#pandas.

import xml.etree.ElementTree as et

data = 'cfb20130831.xml'
xmlf = et.parse(data)
root = xmlf.getroot()

game = root.getchildren()

df = pd.DataFrame(columns=('Team', 'TScore', 'Opponent', 'OScore'))

i = 0
for team in game:
	row = dict(zip(['Team', 'TScore', 'Opponent', 'OScore'], [team[1][0].text, int(team[1].find('offense')[0].text), team[1].find('opponent').text, int(team[1].find('defense')[0].text)]))
	row_s = pd.Series(row)
	row_s.name = i
	df = df.append(row_s)
	i += 1

#2) Describe your dataframe using.describe() method.

df.describe

#3) Choose one numeric variable and transform it into categorical, with 3-5 
#categories. 

bin = [0, 14, 35, 49, 100]
df.TScore = pd.cut(df.TScore, bin)

#4) Get the frequencies for the categorical variable created in part 3.

pd.value_counts(df.TScore

#5) Create an additional variable using mapping and using the categorical variable 
#from part 3. Your map dictionary should have two elements.

pref = {'(0, 14]':'Low scoring', '(14, 35]':'Average', '(35, 49]':'High scoring', '(49, 100]':'Blowout'}
df['Result'] = df['TScore'].map(pref)

#6) Rename two columns in your data using .rename.

df.rename(columns={'TScore':'Team Score', 'OScore':'Opponent Score'})

#7) Extract a 50% training set using cut random permutations of rows (eg. If you 
#have 101 rows in your dataframe, a 50% training set will have about 51 rows).

sample = np.random.permutation(119)
ferro = sample[:60]
ferro = df.take(ferro)

#8) Extract a second 50% training set.

sample = np.random.permutation(119)
ferro = sample[:60]
ferro_df2 = df.take(ferro)

#9) Combine the two training sets into a third dataframe.
#10) Get rid of duplicate rows by using: dataframe_name.drop_duplicates(). What 
#percentage of the rows you have left?
df1 = pd.concat([ferro_df1, ferro_df2])
df1.drop_duplicates


