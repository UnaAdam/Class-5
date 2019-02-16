
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


