# Remove arguments of a function

A simple script that would remove an argument for a given function(used for C functions) in a number of files

## Sample usage:

### For 1 file
the following call will remove the 2nd  argument for every call of the temp_funct function in file tmp.c

    python remove_args.py temp_funct 2  tmp.c
                  
### For a number of files
the following call will remove the 2nd  argument for every call of the temp_funct function in file tmp.c tmp2.c tmp3.c

    python remove_args.py temp_funct 2 tmp.c tmp2.c tmp3.c
