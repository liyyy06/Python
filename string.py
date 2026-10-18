#String
string = """
Hi!

How are you?

Thank you,
Jo
"""
print(string)

course = "Python"
print(course[0])
print(course[-1])
print(course[0:3])

name = "Python"
print(name[1:-1])

# Formatted strings (f-string)
first = "John"
last = "Smith"
message = first +  " [" + last + "] is a coder" #too complicated
msg = f"{first} [{last}] is a coder" 
print(msg)

# String methods
course = "Python code"
print(len(course)) # counting number of characters in string
print(course.upper()) # turning into upper case
print(course.lower()) # turning into lower case
print(course.find("P")) # showing index
print(course.replace("code", "course")) # replace
print("Python" in course) # to check if the string contains some word
