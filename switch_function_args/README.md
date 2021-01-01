# Switch arguments of a function

A simple script that would switch the arguments for a given function(used for C functions)

## Sample usage:

### For 1 file
the following call will switch the 2nd and 3rd argument for every call of the temp_funct function in file tmp.c

    python switch_args.py temp_funct 0 1 tmp.c
if tmp.c contains this code:

    int my_func(a, b, c, d)
after the execution of the script it would have this code:

    int my_func(b, a, c, d)                  
### For a number of files
the following call will switch the 2nd and 3rd argument for every call of the temp_funct function in file tmp.c tmp2.c tmp3.c

    python switch_args.py temp_funct 2 3 tmp.c tmp2.c tmp3.c
