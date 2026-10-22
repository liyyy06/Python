#String
# creating strings -> put [''] pr [""] (opening & closing quotes)
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

# built-in function (len) - returns the number of characters between the opening and closing quotes
print(len("Albert Einstein")) # 15
print(len("123!"))            # 4
print(len(" "))               # 1
print(len(""))                # 0

# operations on strings - add two strings using the + operator
print("Albert" + " " + "Einstein") # Albert Einstein
print("Albert Einstein" + " ")     # Albert Einstein

# string + numeric value
# print("ABC" + 3) # error!
print("Four score and " + str(7) + " years ago")

print(int("a"))   # error
print(float("b")) # error
print(str(3))       # 3

# applying operator * to strings -> string can be repeated using *
print("HA" * 3) # HAHAHA

# assign a string to a variable 
sequence = "ABCDE"
print(len(sequence)) # 5 
new_sequence = sequence + "ABCDG"
print(new_sequence) #ABCDEABCDG

# using special characters in strings
print("that's is not going to work")                # a word contains single quotes should use double quotes around the string
print("that's better")                              # that's better
print('she said, "That\'s hard to read"')           # she said, "That's hard to read"
print('she said, "That' + "'" + 's hard to read."') # she said, "That's hard to read."

# escape sequence
print(len('\'')) 
print('it\'s')
