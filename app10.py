Weight = int(input('Weight: '))
Unit = input('(L)bs or (K)g: ')

if Unit.upper() == "L":
    converted = Weight * 0.45
    print(f"You are {converted} kilos")
elif Unit.upper() == "K":
    converted = Weight * 2.2
    print(f"You are {converted} pounds")

