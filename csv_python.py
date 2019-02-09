#!/usr/bin/env python

import os

#'with' is equal to:
#file_handle = open(myfilename , 'r')
#file_handle.close()

myfilename = "housing.data.txt"
datalist =[]

with open(myfilename, 'r') as file_handle:
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        datalist+=[line_clean.split(' ')]


Attr = [[] for i in range(14)]

for lineindex in range(len(datalist)):
    linedata = datalist[lineindex]

    for numberindex in range(len(linedata)):

        if linedata[numberindex].isdigit():
            linedata[numberindex] = int(linedata[numberindex])


        else:
            linedata[numberindex]=float(linedata[numberindex])

        Attr[numberindex].append(linedata[numberindex])


    #print each line
    #print(linedata)

#or print the whole list.
print(datalist)

print('\n<------------ Attributes Print ------------>')

for index in range(len(Attr)):
    print("\n ------> Attr{0} :\n".format(index))
    print(Attr[index])

