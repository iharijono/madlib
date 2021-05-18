# What is this
This is a README for a simplified demo of madlib app

## Contents
- Remarks on the assignment
- Requirements for deployment & test   
- How to build & test locally 
- How to deploy and test with docker
- Quickstart: Download & Test & Debug 
   
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

## How to build & test locally
- Install all needed python libraries
```
% pip install flask requests

```  
OR better
- Install all python libraries with requirements.txt
```
% pip install -r requirements.txt

```
- Run the python main program or '-h' to get all the optional arguments
```
% python main.py 

```
- Run curl or any other REST API client (postman for example)
```
% python main.py 

```
OR alternatively
- Run test_docker_madlib.sh
```
% ./test_docker_madlib.sh

```
## How to build, deploy and test with docker
- Assuming you have docker installed, build the image
```
% pip install -r requirements.txt

```

## Quickstart: Download & Test & Debug   
- Download the source code from https://github.com/iharijono/madlib.git
```
% git clone https://github.com/iharijono/madlib.git
```     
- Start the app that print the information how to use it:   
```
% python main.py -h
```  
- Start the app (backend) to accept RESTful API request:   
```
% python main.py
```
or with more output:

```
% python main.py -v
```
NOTES: Keeping running 'python main.py -v' for the rest of the tests below.
 
- Run the REST API client ('curl') against the URL (use 'POST' to create a new invoice, 'GET' to retrieve it back)    
```
% TBD
```