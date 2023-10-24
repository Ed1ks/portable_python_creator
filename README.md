# portable_python_creator
Script to convert an Python package into an portable version

## HowTo
1. Download python package from [official Website](https://www.python.org/downloads/)
2. Extract the package in a directory. Example: python3.11.4/
3. Download "prepare-portable-python.py" from this source and put it in the same root directory as python3.11.4
4. Open "prepare-portable-python.py" and edit PYTHONDIR and PYTHONPTHNAME so it meets the downloaded Python version. And Edit DEPENDENCIES for all dependencies which needs to be installed.
6. Run script

## What will happen
1. Directory python3.11.4/Lib/site-packages will be created
2. python<ver>._pth file will be edited
3. pip will be installed in this directory
4. The Dependencies will be installed in this directory

## How To Use Portable Version
You need any other Python version installed on your system.
Then just add following on top of your python lanuch code (assuming its in the same root directory as the directory of step 2):
```
#!python3.11.4\pythonw.exe
```
