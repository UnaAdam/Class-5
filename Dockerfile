FROM ubuntu:16.04
MAINTAINER Dragica Adamovic <UnaAdam.github.io>

RUN apt-get update
RUN cat /etc/lsb-release

#RUN apt-get instay python
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install numpy pandas
ADD . /.
CMD ["python3","csv_python.py"]

