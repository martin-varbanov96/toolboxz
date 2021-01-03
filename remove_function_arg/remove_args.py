import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("function_name", type=str,
                    help="function name whose arguments will be switched")
parser.add_argument("index", type=int,
                    help="first argument to be switched")
parser.add_argument('files', metavar='files', type=str, nargs='+',
                    help='files in which function arguments will be switched')

args = parser.parse_args()
def switch_function_args(func_name, args, index=0):
    function_call_pattern = "{}[^\)]+".format(func_name)
    for file in args:
        has_function = False
        file_content = ""
        with open(file, "r") as f:
            file_content = f.read()
            if(func_name in file_content):
                has_function = True
        if(has_function):
            for current_function_structure in re.findall(function_call_pattern, file_content):
                current_arguments = re.split("\(", current_function_structure)[1]
                current_arguments = re.split(",", current_arguments)

                # remove the specified argument
                del current_arguments[index]

                fixed_arguments = ",".join(current_arguments)
                fixed_function_structure = "{}({}".format(func_name, fixed_arguments)
                old_struct_pattern = current_function_structure.replace("(", "\(")
                file_content = re.sub(old_struct_pattern, fixed_function_structure, file_content)
            with open(file, "w") as f:
                f.write(file_content)
                    
switch_function_args(args.function_name, args.files, index=args.index)

