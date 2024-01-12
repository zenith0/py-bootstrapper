# How it works and current limitations

## Input:
1. args[1]: your projectname
2. args[2]: the project destination,  -prj_dst <path>

Call the bootstrap.py with the root folder where you want to create the python project. Input can be:
1. an absolute path (unix + win sup, if the folder path starts with "drive:\\ or / it is considered an absolute path)
2. a relative path (not 1.), just create a projet on the fly and move later  
3. empty - the current path is taken and a python project is bootstrapped