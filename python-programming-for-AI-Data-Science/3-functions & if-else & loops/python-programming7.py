# True-False 

border = 5000

border == 4000 

border == 5000

5 == 4

# if

border = 50000

income = 60000

if income < border:
    print("Income is less than border.")
    
if income > border:
    print("Income is greater than border.")


# else

border = 50000
income = 50000

if income > border:
    print("Income is greater than border.")
else:
    print("income is less than border.")
    
if income == border:
    print("Income is equal to the border.")
else:
    print("income is not equal to the border.")

# elif

border = 50000
income1 = 60000
income2 = 50000
income3= 35000

if income2 > border:
    print("Congrats!")
elif income2 < border:
    print("Warning!")
else:
    print("income is equal to the border.")
    
# user interactive mini app

border = 50000
store_name = input("What is the store name?")
income = int(input("Enter your income:"))

if income > border:
    print("Congrats!" + store_name + " You won a promotion.")
elif income < border:
    print("Warning! Low income." + str(income))
else:
    print("Income is equal to the border.")

# Loops - for

student = ["john","jamie","steve","layla"] 
student[0]
student[1]

for i in student:
    print(i)

