import math

value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal = float(input("Enter a decimal measurement: "))

power = math.pow(value, exponent)
square_root = math.sqrt(value)
ceil_val = math.ceil(decimal)
floor_val = math.floor(decimal)

print("\nResults")
print(f"Value : {value}")
print(f"Exponent : {exponent}")
print(f"Power (pow) : {power}")
print(f"Square Root (sqrt) : {square_root}")
print(f"Decimal Value : {decimal}")
print(f"Ceil Value : {ceil_val}")
print(f"Floor Value : {floor_val}")