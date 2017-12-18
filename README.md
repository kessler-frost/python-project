# Python Script To Ease Development

## Introduction

Generally when a certain developer wants to run a code from Github he has to deal
with a lot of functions definition of which is hard to find given a large number of
files. Similarly, there are certain changes which are to be required if one wants to
convert a python 2 file to a python 3 one, the syntax changes are prominent ones.
There may be a number of libraries which must be required for the code to run
properly which might not be present on this particular developer’s local machine.

Again for new developers who have just started using python, they may be required
to install pip package manager in order to facilitate the package installation and
uninstallation process which becomes a vital part of the development work flow in
future. When developing for open source projects there might also be a requirement
to keep the pep8 formatting in order to maintain uniformity of code across all the
files in that project.

All of the above issues were encountered by us when we started to code in python.
Thus, we looked for a solution to some if not all of these above mentioned problems
and came up with a easy to use and interactive script to facilitate the developer’s
workflow, such that he can focus on development and not on these trivial things
which can be automated.

## Features

We aimed to create a script which when executed upon a python file or multiple
files will be able to perform a number of operations making the work of developers
easy. These operations include :-

1. Detects the python version being used, 
2. Lists the packages used,
3. Offers to installed not installed packages,
4. Checks if pip is installed or not and offers to install if not already installed,
5. Creates a method source tree containing all the functions and grouped together according to each’s 
parent class and file (when multiple files are given),
6. Verifies if the given file is written according to pep8 guidelines, if not outputs the pep8 errors
to a new file,
7. Converts a python 2 file to a python 3 file. The caveat while running this script
is that the interpreter being used must have a python version more than or equal to 3.

## Instructions to Run

In order to run this script open a terminal/cmd session in the directory in which the
files are present in, and copy the script there, then execute command :-

```
python prp_script.py [-A] {file_name_1.py file_name_2.py ...}
```
`[-A]` flag is used if all the python files in current directory are to be operated
upon.
