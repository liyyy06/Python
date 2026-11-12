def convert_to_celsius(fahrenheit):
    """
    Return the number of Celsius degrees equivalent to fahrenheit degrees.
    """
    return(fahrenheit - 32) * 5.0 / 9.0

def above_freezing(celsius):
    """
    Return True if temperature is above freezing
    """
    return celsius > 0

print(convert_to_celsius(20)) # -6.666666666666667
print(convert_to_celsius(59)) # 15.0

if __name__ == "__main__":
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print("It is above freezing")
    else:
        print("It is below freezing")