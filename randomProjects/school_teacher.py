lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers): # define the average function
    total = sum(numbers) # Add the sum of a list
    avg = float(total)/len(numbers) # divide total with len #
    return avg # Return the avg

def get_average(student):
    # 1. Get the average of the key : Homework
    homework = average(student["homework"])
    # 2. Get the average of the key : Quizzes
    quizzes = average(student["quizzes"])
    # 3. Get the average of the key : Tests
    tests = average(student["tests"])
   
    # Multiply the variables
    total = homework * 0.1, quizzes * 0.3, tests * 0.6
    # Sum the list and then return the value
    return sum(total)

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

get_letter_grade(get_average(lloyd))

def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)
       
print get_class_average(students)
print get_letter_grade(get_class_average(students))
