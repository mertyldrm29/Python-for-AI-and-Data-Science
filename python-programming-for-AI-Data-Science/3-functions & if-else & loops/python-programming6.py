# introduction to functions 

print("a","b", sep = "_")
?print

len("a")

# mathematical operations

4*4
4/4
5-1
6+3
3**2
3**3

# creating a function

def square(x):
    print(x**2)
    
square(3)

# output with information

def square(x):
    print("The square of the given number is:" + str(x**2))
square(4)

def square(x):
    print("Given number:" + str(x) + ", The square of the given number is: " + str(x**2))
square(4)

# another alternative

def square2(y):
    print("Given number:",y,"The square of the given number is:", y**2)
square2()

# creating function with two arguments

def multiply(x,y):
    print(x*y)
multiply(2, 3)

# predefined arguments
def multiply(x,y=1):
    print(x*y)
multiply(3)

# sorting arguments

# predefined arguments
def multiply(x,y=1):
    print(x*y)
multiply(y= 2,x =3)
multiply(4,5)


# using functions' outputs as inputs

def street_pole(temperature,humidity,battery):
    print((temperature+humidity)/battery)

output = street_pole(25, 40, 70)
output
print(output)
street_pole(25, 40, 70)*9

def street_pole(temperature,humidity,battery):
    return((temperature+humidity)/battery)

street_pole(25, 40, 70)*9
output = street_pole(25, 40, 70)
output
print(output)

# local and global variables

x = 10
y = 20

def multiply(x,y):
    return x*y
multiply(2, 3)

# changing global domain from local domain

x = []

def add_item(y):
    x.append(y)
    print(str(y) + " added to the list.")
add_item(4)
add_item("jason")
x

