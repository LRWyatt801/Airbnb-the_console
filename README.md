# Console (HBNB)

![banner_image](https://camo.githubusercontent.com/0abfd1a3534470d279dd6eaca57e0b4b81e23fb77afd81483d470c2f63ab51d3/68747470733a2f2f692e696d6775722e636f6d2f4d5171334142632e706e67)

The HBNB Console, a backend tool for the Atlas AirBnB project


## Description

this is a description of the HBNB console, slightly more in depth with a few small examples and images of how it works. Specifically does not get into how to use it, that comes below, this area is more to showcase the projects utility 


## Installation

This program was developed in Python on Ubuntu Linux, and is meant to work on a Linux distribution- if you are running Windows look into installing [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

> In your terminal, run ```git clone https://github.com/LRWyatt801/atlas-AirBnB_clone.git```
> Once downloaded, run the command ```./console.py``` to begin



## How to use

Here's a list of commands our console supports:

- ```EOF```     - exits the console
- ```quit```    - also exits the console
- ```help```    - assists with commands
- ```create```  - creates a new instance (state, city, listing, etc)
- ```show```    - show will print a specific instance
- ```destroy``` - destroy + className + id will remove that instance from the program
- ```all```     - all + className will print all instances of a class, shows everything with no arguments
- ```update```  - update + className + id will update that specific instance

> [!IMPORTANT]
> Most of these commands require entering both the className of the instance and the id in question in order to access, as shown: 
> ex. 1: ```create listing 1234-1234-1234```
> ex. 2: ```show listing 4567-4567-4567```

## Dependencies

this is a table and description of all the modules we used to make the program, with links to describe how they're used

| Python module                                                         | Description                |
| -----------                                                           | -----------                |
| [cmd](https://docs.python.org/3.4/library/cmd.html)                   | The Command Module         |
| [uuid](https://docs.python.org/3.4/library/uuid.html)                 | Unique ID generator        |
| [datetime](https://docs.python.org/3.4/library/datetime.html)         | Date/time formatter        |
| [unittest](https://docs.python.org/3.4/library/datetime.html)         | Testing and QA module      |


## Dataflow

The HBNB console doesn't depend on a strict hierarchy of monolithic Dictionaries, rather it connects separate instances through unique ids

```Python
listing = {
    'id' = '1234-1234-1234-1234',
    'user_id' = '3456-3456-3456-3456'
    'city_id' = '7890-7890-7890-7890'
}

city = {
    'id' = '7890-7890-7890-7890'
    'state_id' = '5678-5678-5678-5678'
}

state = {
    'id' = '5678-5678-5678-5678'
}
```
All the above classes inherit from a common class ```Basemodel``` which gives each class a common pool of methods and attributes to pull from. Here's a diagram of how these different classes interact with one another: 

![dataflow](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240601%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240601T021325Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9223da17c56396026e7f8cf4c7300d7f7aa2a35019c63a79e3aff64e89f38f98)

## About the developers

Logan Wyatt and Davey Hays are two Tulsa based developers and current students at Atlas Tulsa (formerly: Holburton). 