
#!/usr
# Step 1 load a dataset from a file
# Step 2 organize that file so we can access columns and rows easily
# Step 3 compute some summary statistics about data
# Step 4 print those summary statistics


# 1. load a dataset from a file 
# 1a. accept arbitrary filename as argument
# 1b. load the file

from argparse import ArgumentParser

parser=ArgumentParser(description=' A CSV reader + stats maker')
parser.add_argument('csvfile', 
          help='Path to the input csv file.') 

parserd_args = parser.parse_args()
# print(parserd_args)
# print(parserd_args.csvfile)

myfile = parserd_args.csvfile


import os 
import os.path as op

#if os.path.isfile(myfile):
#   print("ya")

#else:
#  print("oops")

assert os.path.isfile(myfile), "please give us a real file"

#if not os.path.isfile(myfile):
   #raise ValueError("not a valid 

print('The file exist')

#1a finilized
#1b 

import pandas as pd

data = pd.read_csv(myfile, sep='\s+|,', header=None)
print(data.head())

#for item in print dir(data):
#  print(item)

print(data.shape)

#2. organzie a file so we can access columns and rows of it easily

#2a. access any row "pandas access data by row" 
#print(data.iloc[3:5,:])

#2b. access any column "pandas acces by colum"
#print(data.iloc[:3, -2:])

#2c. access any value "pandas acces specific data based on location"
#print(data.iloc[3,4])

import numpy as np

print(np.mean(data))
print(np.std(data))



bostonDF = pd.DataFrame(data)
#print(bostonDF.head())

bostonDF = bostonDF.rename(columns={0: 'CRIM', 1: 'ZN', 2:'INDUS', 3:'CHAS', 4:'NOX', 5:'RM', 6:'AGE', 7:'DIS', 8:'RAD', 9: 'TAX', 10:'PTRARIO', 11:'B', 12:'LSTAT', 13:'PRICE'}) 
print(bostonDF.head())

import matplotlib.pyplot as plt
import sklearn
import seaborn as sns 
sns.set(color_codes=True)

correlation_matrix = bostonDF.corr().round(2)
heatmap = sns.heatmap(data=correlation_matrix, annot=True)
myfig = heatmap.get_figure()
myfig.savefig('output.png')
plt.close()


#Histogram for each column
for col in bostonDF: 
   idx= bostonDF.columns.get_loc(col)
   sns.distplot(bostonDF[col].values,rug=False,bins=50).set_title("Histogram of {0}".format(col))
   plt.savefig("./{0}_{1}.png".format(idx,col), dpi=100)
   plt.close()




#Scatterplot and a regression line for each 2 columns
   for nxt_col in bostonDF.iloc[:,idx+1:]:
 
      sns.regplot(bostonDF[col], bostonDF[nxt_col], color='g')
      plt.xlabel('Value of {0}'.format(col))
      plt.ylabel('Value of {0}'.format(nxt_col))
      plt.title ('Scatter plot of {0} and {1}'.format(col,nxt_col))

      plt.savefig("./{0}_{1}_{2}".format(idx,col,nxt_col), dpi=200)
      plt.close()
