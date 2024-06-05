# Console (HBNB)

![banner_image](https://camo.githubusercontent.com/0abfd1a3534470d279dd6eaca57e0b4b81e23fb77afd81483d470c2f63ab51d3/68747470733a2f2f692e696d6775722e636f6d2f4d5171334142632e706e67)

The HBNB Console, a backend tool for the Atlas AirBnB project


## Description

![HBNBexampleouse](https://github.com/LRWyatt801/atlas-AirBnB_clone/assets/63436710/a2248de1-c3cc-48ce-bc94-f77d39df831c)

The HBNB console is a tool to access and manipulate the data of the greater HBNB website directly. It adds basic CRUD functionality (create, read, update and delete) to all the basic data structures of the website. 

## Installation

This program was developed in Python on Ubuntu Linux, and is meant to work on a Linux distribution- if you are running Windows look into installing [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

> In your terminal, run ```git clone https://github.com/LRWyatt801/atlas-AirBnB_clone.git```
> Once downloaded, run the command ```./console.py``` to begin



## How to use

Here's a list of commands our console supports:

- ```EOF```     - exits the console
- ```quit```    - also exits the console
- ```help```    - assists with commands ```ex. help create```
- ```create```  - creates a new instance (state, city, listing, etc) ```ex. create User```
- ```show```    - show will print a specific instance ```ex. show User 1212-1212-1212-1212```
- ```destroy``` - destroy + className + id will remove that instance from the program ```ex. destroy User 1212-1212-1212-1212```
- ```all```     - all + className will print all instances of a class, shows everything with no arguments ```ex. all User```
- ```update```  - update + className + id will update that specific instance ```ex. update User 1212-1212-1212-1212 email 'email@email.com'```

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
{'Place.1212-1212-1212-1212' : {
    'id': '1234-1234-1234-1234',
    'user_id': '3456-3456-3456-3456',
    'city_id': '7890-7890-7890-7890'
},
'City.2323-2323-2323-2323':  {
    'id': '7890-7890-7890-7890',
    'state_id': '5678-5678-5678-5678',
    'name': 'Tulsa'
},
'State.3434-3434-3434-3434':  {
    'id': '5678-5678-5678-5678',
    'name': 'Oklahoma'
}}
```
All the above classes inherit from a common class ```Basemodel``` which gives each class a common pool of methods and attributes to pull from. Here's a diagram of how these different classes interact with one another: 

![dataflow](https://github.com/LRWyatt801/atlas-AirBnB_clone/assets/63436710/47c2164c-4e87-4167-b70a-c3d5a830f29b)

## About the developers

Logan Wyatt and Davey Hays are two Tulsa based developers and current students at Atlas Tulsa (formerly: Holburton). 