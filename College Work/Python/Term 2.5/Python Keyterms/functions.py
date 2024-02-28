global_variable = "Hello"

def function_example(param):
    global global_variable
    global_variable = global_variable + " " +param
    return global_variable

argument = input("Input argument: ")
function_example(argument)
print(global_variable)
