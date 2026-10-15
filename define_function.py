#Defining our own function
# def function_name(parameters) : #parameters = variable
#     return (expression)

#Using local variables for temporary storage
def quadratic(a, b, c, x) : 
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third
#quadratic(2,3,4,0.5)
print(quadratic(2,3,4,0.5))

def f(x) :
    x = 2 * x
    return x
# x = 1
# x = f(x+1) + f(x+2)
x = 1
print(f(x+1)+f(x+2)) #first, put x=1 on the function f(x+1) -> f(2) -> f(2)=4

# A recipe to design a new functions
## What do you name the function?
## What are the parameters?
## What does it return?

def days_difference(day1, day2) : 
    return (day2-day1)
print(days_difference(200, 224))
