# Script template



## What is this?
This is a template script based on which new scripts can be created.
It includes in-house libraries (e.g. for interacting with Boom/Amigo).
It demonstrates an architecture that is suited for 500-1000 lines script.


## What is the goal?
The goal is to make scripts faster.
The goal is to make scripts more maintanable.
The goal is to make scripts more reliable.
The goal is to make an outline which can be leveraged when making new scripts.


## What are the key features?
 - Logging set up which reports errors from external libraries and debug from itnernal libraries and scripts to logs/main.log
 - Testing set up with unit tests.
 - Code split into logical multiple file structure.
 - Internal libraries with most commonly needed functions for business.


## How to update the script?
- If you make a function that you anticipate will be used by more than one script add it to the internal library.
- If you make an architectural change that makes the overall script ecosystem better, update this template.
- Make updates broadly applicable to scripts in general, anything that relates to a single script should be kept exclusively to its repository/


## 2025, Dimitrije Mikarić