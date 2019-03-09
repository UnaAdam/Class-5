A)INSTRUCTIONS FOR BUILDING 

B) SHOWING US THAT IS EXITS/WHEN IT WAS MADE

C) RUNNING YOUR DOCKER FILE

We need to create a directory on our computer 
mkdir Git

Go to the created directory
cd Git

Conect with a GitHub
git clone weblink

Create file called Dockerfile
nano Dockerfile 

Connect to unbuntu, install the Python 3, and libraries (panda and numpy), copy files 
Docker and runnung them 
FROM unbuntu:16.04
MAINTAINER Dragica Adamovic <UnaAda.github.io>

RUN apt-get update
RUN cat /etc/lsb-release

RUN apt-get install -y python3-pip
RUN pip3 install numpy pandas
ADD . /.
CMD ["pythin3","csv_python.py"]

Building the app
docker build -t d_adamov/my-new-image ./

To see where is our build image 
docker images

Run the app
docker run -ti d_adamov/my-new-image 
 

Continous integration (CI) is usefull when more than one developer work simutaneously on the same application. 
Developers create a multiple 
brenches when they work on the project. So it my be the case that the code on an unmarged brench looks less and less like 
the code on a master branch. This could potentially caused the problems when times comes to merge this two brenches. The function of the Continous 
integration is to make this merging more easier.


Create Pseudocode  - Homework #5

A) LOAD

   a.0 accept arbitrary filename as argument
       a.0.1 import library ArgumentParser

   a.1 load the file
 

B) 'ORGANIZE'

   b.0 organize the file so we can access the columns and rows easily
       b.0.1 we can import panada library
       b.0.2 then we can arrange the data in the tables with default names of columns and rows (e.g. 0, 1, 2, 3, 4, etc.)

C) COMPUTE SUMMARY STATISTiCS
   c.0 for instance see the minimum, maximum and average values of the columns 
   c.1 also we can print mode, wich is the value that appears the most in our data
   c.2 see the deviation of the data - standard 

D) VIZUALIZE THE DATA (1-feature, one column at the time, i.e. histogram and save the figures to the file) - we can either build up the plots in the python 
or use the libraries. For the purpose of this study, we will import library that will allow us to more easily vizualise given data. 

   d.0 first, we need to import the library, for instance matplotlib
   d.1 specify the 'interface' to matplotlib - histogram 
   d.2 specify which axis he needs to take - we need to create a loop, so he creates a histogram for each column
   d.3 then we can label 'y' axis 
   d.4 also, we can label 'x' axis
   d.5 specify the name of the plot
   d.6 specify the size of the text
   d.7 determine the text propreties, like size, type, etc.
   d.8 determine the frequency, or the 'density' of the plot
   d.9 set the limit of the y-axis
   d.10 create an image, figure
   d.11 plot to file

Note: a plot of a histogram uses its bin edges on the x-axis and the corresponding frequency on y-axis. For instance, we can set the passing bin='auto'
So 

E) VIZUALIZE THE DATA (2-feature, two columns, at the time), i.e. scatter plot, and save the figures to the file)
   e.0. determine   



F) FOR ADDING HEADER DATA TO THE TABLE 
   f.0 we need to rename the columns
       f.0.1 for each column we need to provide the name, pandas lybrary have the option for renaming 
       f.0.2 print the table, or save it as a file 

G) ADDITIONAL TYPE OF PLOT FOR VISUALIZING 2 OR MORE FEATURES AT THE TIME (use matplotlib for plotting)
   g.0 for instance, we can print the correlation matrix 
       g.0.1 import matplotlib 
       g.0.2 we need to print our table as a coorelation matrix, so we will find a correlation coefficients between variable
             so each cell in a table will show the correlation between variables. This way we will summarize data and be able to go to more deeper analysis, see the patterns. 

       g.0.3 create a heat map from the data in a correlatio matrix, so data from the correlation matrix are used for heat map
       g.0.4 create from heat map a figure
       g.0.5 save as figure, for instance image format png
 





   





  



0 Load data
1 Format data
2 Summary statistics
  2.5 Add the headers 
3 Look at data
  3.1 Plot data on ther own 
      3.1.1 For each colum 
      3.1.2 Get variablus
      3.1.3 Plot hystogram 
  
  3.2 Plot pairs "2xfor"
      3.2.1 For each pair of columns
      3.2.2 Plot
    
  3.3 Had another plot data
 

"{0}words".format()


HOMEWORK FOR WEEK 7

the best to images for interpreting the data are Output.png & Pairplot.png. The first one is a heatmap, 
a correlation matrix that measeure the linear relationship between the variables. The second image is 
created with seaborn library, and is also relationship matrix, that shows graphically correlation between 
different features. Coorelation coefficients could range from -1 to 1, and the more value is closer to 
the 1, it means that there is a strong relationship between variables. For instance, if we look at the 
price as a main feature, we can see that RM (0.70) and LSTAT (0.74) have hight correlation. 
Also, of we werify on the other image file, Pairplot.png, we will see that of RM increases the prices 
increase as well. Also, if ALSTAT increases the prices decreases. For the firts feature it look like 
we can feat the straight curve, while in the second one, it would be a non-linear curve.  
