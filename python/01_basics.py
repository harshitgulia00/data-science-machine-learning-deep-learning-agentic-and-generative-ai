print("Hello, World!!")
# This is a single line comment
"""


            This is a multi-line comment


 """


# numbers and floats
a = 10
b = 20
c = a + b
print("The sum of a and b is:", c)
type_of_c = type(c)
print("The type of c is:", type_of_c)


#    boolean
a1 = True
a2 = False
type_of_a1 = type(a1)
type_of_a2 = type(a2)
print("a1 is:", a1)
print("a2 is:", a2)
print("The type of a1 is:", type_of_a1)
print("The type of a2 is:", type_of_a2)


#      strings
str2 = "harshit"
str1 = "harshit"
print("The string is:", str2)
print("The type of str2 is:", type(str2))
print("The string is:", str1)
print("The type of str1 is:", type(str1))
print(str2 + str1)

# complex numbers
a = 2 + 3j
b = 4 + 5j
print("The complex number a is:", a)
print("The complex number b is:", b)
print("The real part of a is:", a.real)
print("The imaginary part of a is:", a.imag)
print(a+b)

# Dynamic Typing
a = 10
a = "Now I'm a string"
print(a)

#strong typing
a = 10  
b = "eejsfg"
# This will raise a TypeError because you cannot add an integer and a string
# c = a + b


# Type Casting
a = "10"
b = "20.5"
c = float(a) + float(b)
print(c)


#string formatting
name = "Alice"
age = 30
print("My name is {1} and I am {0} years old.".format(age, name))



# input from user
name = input("Enter your name: ")   
age = int(input("Enter your age: "))
print("name is :"+ name + " age is :"+ str(age))