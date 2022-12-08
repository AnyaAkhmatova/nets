FROM ubuntu:20.04
RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install python3.8 -y
RUN apt update
RUN apt install iputils-ping
ADD hw2.py /home
RUN chmod +x /home/hw2.py
WORKDIR /home
