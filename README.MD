# Script template



## What is this?
This is a template script based on which new scripts can be created.
It includes in-house libraries (e.g. for interacting with Boom/Amigo).
It demonstrates an architecture that is suited for 500-1000 lines script. <br>


## What is the goal?
The goal is to make scripts faster. <br>
The goal is to make scripts more maintanable. <br>
The goal is to make scripts more reliable. <br>
The goal is to make an outline which can be leveraged when making new scripts.<br>


## What are the key features?
 - Logging set up which reports errors from external libraries and debug from itnernal libraries and scripts to logs/main.log
 - Testing set up with unit tests.
 - Code split into logical multiple file structure.
 - Internal libraries with most commonly needed functions for business. <br>


## How to update the script?
- If you make a function that you anticipate will be used by more than one script add it to the internal library.
- If you make an architectural change that makes the overall script ecosystem better, update this template.
- Make updates broadly applicable to scripts in general, anything that relates to a single script should be kept exclusively to its repository. <br>

#### How to document the scripts?
- Assume that you are writing to a competent but unfamiliar to script engineer.
- Document in a line or two for every function: input, output, note/special restriction.
- Document as little as possible.<br>

#### How to write tests?
- Test each function with: expected input, out of range input, wrong input type.
- Prioritize thorough testing of the internal libraries as they will be reused and having them in working order is necessary for the whole ecosystem.
- Don't write tests for tests' sake. Be intentional.<br>

#### How to log? <br>
- Each log adds visual clutter to the function. Log only when potential info is more valuable than the clutter detracts.
- Log different logic flows, so upon seeing the log it is clear which branch the code went into.
- Only log erros and above for the external libraries
- Within a single logic flow through a log if it is really long, so it can be determined which part of the logic failed.


<br>

## 2025, Dimitrije Mikarić