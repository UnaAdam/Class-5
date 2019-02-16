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


Create Sudocode

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


