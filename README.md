## Project : AirBnB Clone - Console
## authors : Mohamed EL AQAOUI & Atmane Baria
Project Overview :
Welcome to the AirBnB clone project! this project is a good challenge for us to test our python knowledge during this learning The primary objective is to develop a command interpreter to manage various objects within the AirBnB application.


# Command line

The command interpreter serves as a tool for interacting with AirBnB objects. Similar to a shell, it enables the user to:

Create new objects (e.g., User, Place)
Retrieve objects from various sources (files, databases)
Perform operations on objects (count, compute stats, etc.)
Update attributes of an object
Destroy an object

# Execution Modes

The console supports both interactive and non-interactive modes. In interactive mode, it operates as follows:

----------------------------------------------------------
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
----------------------------------------------------------

## Non-interactive mode, resembling the Shell project in C, is also supported:

----------------------------------------------------------
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
---------------------------------------------------------
## Running Tests :
$ echo "python3 -m unittest discover tests" | bash
