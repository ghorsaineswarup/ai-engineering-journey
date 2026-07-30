a = 10
b = 2

try:
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Erroe : You cant divide by zero!")
except TypeError:
    print("Error: You cant divide a number by a string!")

print("Program continues running after the error...")