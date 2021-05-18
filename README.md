# What is this
This is a README for a simplified demo of madlib app (https://gist.github.com/porkloin/289a641b9f3b6a22c48a5913cd1aede6)

## Contents
- Remarks on the assignment
- Requirements for deployment & test   
- Download the source code   
- How to build & test locally 
- How to deploy and test with docker
 
## Remarks on the assignment
- For this task, 
  It focuses on the implementation of REST API, and requests library to invoke URL  

## Requirements for deployment & test  
- Python 3.x.x and pip (refer to how to install python for your development environment)  
- python libraries: flask and requests
- Internet connection to public (URLs)
- Docker
- curl
- OPTIONAL but nice to have: virtualenv    

## Download the source code   
- Download the source code from https://github.com/iharijono/madlib.git
```
% git clone https://github.com/iharijono/madlib.git
```     

## How to build & unit test & test locally
- Assuming Python 3.x.x + pip are installed, Install all needed python libraries
```
% pip install flask requests

```  
OR better
- Install all python libraries with requirements.txt
```
% pip install -r requirements.txt

```
- To run unit tests:
```
python test_api.py
```
- To test the app, run the python main program or '-h' to get all the optional arguments
```
% python main.py 

```
- Run curl or any other REST API client (postman for example)
```
% curl 127.0.0.1:9000/madlib; echo

```
OR alternatively
- Run test_docker_madlib.sh
```
% ./test_docker_madlib.sh

```
## How to build, deploy and test with docker
- Assuming you have docker installed, build the image with the tag <user>/modlib where user is your user id (on github for example)
```
% docker build -t <user>/madlib .

```
- Verify that the image has been built locally with the tag, for example:
```
% docker images
REPOSITORY         TAG       IMAGE ID       CREATED              SIZE
iharijono/madlib   latest    46922f1588c9   About a minute ago   91.4MB

```
- OPTIONAL and probably not for YOU, tag the image, relogin to prepare to push to dockerhub.com as I did
```
% docker tag 46922f1588c9 iharijono/modlib
% docker login (you need to register yourself on dockerhub.com and get uid and password to login)
% docker push <user>/modlib

```
- Assume <user> is iharijono, run the container from the image
```
% docker run -p 9000:9000 --name modlib_c iharijono/madlib

```
- Run curl or any other REST API client (postman for example)
```
% curl 127.0.0.1:9000/madlib; echo

```
OR alternatively
- Run test_docker_madlib.sh
```
% ./test_docker_madlib.sh

```