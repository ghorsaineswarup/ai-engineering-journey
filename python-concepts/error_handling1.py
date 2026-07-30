#ValueError
#age=int("Namaste")
#print(age)

#fixed code
try:
    age=int("Namaste")
    print(age)
except ValueError:
    print("Error: Thats not a valid number!")

print("program continues running...")    