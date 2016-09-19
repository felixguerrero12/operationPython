# Take in a list of numbers and does the calculation for by calling the definition.

def average(numbers): # define the average function
    total = sum(numbers) # Add the sum of a list
    avg = float(total)/len(numbers) # divide total with len #
    return avg # Return the avg
