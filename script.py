values = [] # creating an empty list

userInput = 0 # initial value

while (userInput != ""):
    userInput = input("Enter a number or press Enter to quit: ")
    if (userInput != ""):
        try:
            n = float(userInput)
            values.append(n) # adding the inputs to the list
        except ValueError: 
            print("INVALID INPUT. Please try again.") # when error is encountered

sum = sum(values) # sum of values
ave = sum/len(values) # average of values

print("The sum is", sum)
print("The average is", ave)



