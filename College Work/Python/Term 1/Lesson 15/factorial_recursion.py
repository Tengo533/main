# Function to calculate fibonacci - relies on recursion
def fibonacci(ip):

    #print("fibonacci() called with ip value = " + str(ip))
    
    if ip<0:
        print("ERROR incorrect ip value 0")
    elif ip==1:
        return 0
    elif ip==2:
        return 1
    else:
 
        return ( fibonacci(ip -1) + fibonacci(ip -2) )




#---
# Main program to call factorial function
#---

# Read input from keyboard, prompting user for a number
# nb: keyboard input is a string hence need to cast to a number
my_num = int( input("Pls enter a value:\n") )

# Call factorial function
fib = fibonacci(my_num)

# Print result, nb: str() is to cast number to a string
print ("The fibonacci of " + str(my_num) + " is " + str(fib))