import random # Imports the module for generating random numbers

pw = "" # Declaring the password variable outside of the loop so that it can be accessed globally by different instances of the loop.
wow = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] # Declaring an "array" or list of possible characters that can be put in the password. This can be modified to add or take away more.
idx = len(wow) # idx is referring to "index", but we use that same variable name later so we'll just put this as idx. This gets the length of "wow", which is the list of possible characters. You'll see why this will be useful later on.
times = 0 # Declaring the times variable outside of the loop so that it can be accessed globally by different instance of the loop.
index = 0 # Declaring the times variable outside of the loop so that it can be accessed globally by different instances of the loop.
option = "" # Declaring the option variable outside of the loop so that it can be accessed globally by different instances of the loop.
repeat = True # Determines whether the loop of generating passwords should continue or not.
print("Generating password...") # Initial console text the user will see, which will be preceded by the generating of a password.
while repeat == True: # Declaring the loop as to which passwords will be generated.
    pw = "" # Clearing the password variable so they don't generate on top of each other.
    times = 0 # Clearing the times variable so that the loop can proceed without times remaining 14, which would then not allow the loop to run properly causing the password to not generate.
    while times < 14: # Replicating the function of a for loop since Python doesn't have one.
        index = random.randint(0, idx - 1) # Setting index to a random number between 0 and the length of the character list.
        pw = pw + wow[index] # Adding the current value of pw with the character in thelist that has been selected by the randomly generated number.
        times = times + 1 # Increasing the value of times by 1 so that way it will know when to stop, otherwise we'd have an infinite loop because the while condition would never be met.
    print("Finished generating password.") # Printing that it finished generating. These lines of code will be run once the while loop has finished.
    print("Password: " + pw) # Printing the generated password.
    print("Do you want to generate another password? (Y/N)") # Asking if the user would like to generate another password.
    option = input() # Getting user input.
    if option == "N" or option == "n" or option == "No" or option == "no": # If they say no:
        print("Thank you for using String's password generator.") # Tell the user thanks for using this generator.
        repeat = False # Turn the repeat variable False so that the initial while loop condition will no longer be met, hence the password generator loop will be cancelled, hence no more passwords will be generated.
    elif option == "Y" or option == "y" or option == "Yes" or option == "yes": # If they say yes:
        print("Generating new password...") # Simply print generating a new password and the loop will take care of the rest.
    else: # If they say none of the options:
        print("Sorry, we didn't quite get that, you answered with " + option + " which is not valid between yes or no.\nGenerating new password...") # Tell the user they did not input a valid answer and simply resort to generating another password.
