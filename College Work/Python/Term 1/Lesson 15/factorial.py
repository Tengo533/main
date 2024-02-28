# Function to calculate the factorial of a number - relies on recursion
def factorial(ip):

    #print("factorial() called with ip value = " + str(ip))

    # exit condition so dont keep recursing forever
    if(ip==1):
        return 1

    # Return current value multiplied by next value in sequence
    # - recursively call this function using next value
    #  e.g if ip==5 then calls self with ip==4    
    return ip * factorial(ip-1)


# Test code to verify the factorial function works correctly
def test_factorial():
    test_val = 6
    correct_answer = 720     # 6x5x4x3x2x1 = 720

    test_result = factorial(test_val)

    # Check our function returned the correct factorial value
    if test_result == correct_answer:
        print("PASSED TEST")
    else:
        print("FAILED TEST")


#---
# Main program to call factorial function
#---

# Test factorial function to confirm works correctly
test_factorial()

# Read input from keyboard, prompting user for a number
# nb: keyboard input is a string hence need to cast to a number
my_num = int( input("Pls enter a number to factorise:\n") )

# Call factorial function
# TODO call the factorial function with the value
#      you read in from the keyboard. Capture the 
#      value returned by the function into a variable
#      called "fac" 
fac = factorial(my_num)
# Print result, nb: str() is to cast number to a string
print ("The factorial of " + str(my_num) + " is " + str(fac))