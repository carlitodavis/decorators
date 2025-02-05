def my_decorator(func):
    def wrapper(*args):
        print("Average before calling the function")
        result = func(*args)  
        print("After calling the function", result)
        return result  
    return wrapper 

@my_decorator
def calcAverage(grades):
    print("Inside the function, calculating average")
    if not grades:
        return 0  
    return sum(grades) / len(grades)  

grades = [85, 90, 78, 92, 88]
average = calcAverage(grades)
print("Final returned value:", average) 