try:
    age = int(input("Age:"))
    income = 20000
    risk = income / age
    print(age)
except (ValueError, ZeroDivisionError):
    print("Invalid Value")
