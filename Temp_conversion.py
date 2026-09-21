
def tempConversion(c):
    f = (c * 9/5) + 32
    return f

c = int(input("Temperature in Celsius: "))
f = tempConversion(c)
print("Temperature in Fahrenheit: ", f)