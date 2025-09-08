
while True:
    fahrenheit_or_celsius = input("What you want convert(F/C): ")
    if fahrenheit_or_celsius == "C":
        temp2 = input("What temperature in Celsius: ")
        fah = (int(temp2) * 1.8) + 32
        print(fah)
        break
    elif fahrenheit_or_celsius == "F":
        temp1 = input("What temperature in Fahrenheit: ")
        cel = (int(temp1) - 32) * 0.5555 
        print(cel)
        break
    else:
        print("Something went wrong. Try again")
        

