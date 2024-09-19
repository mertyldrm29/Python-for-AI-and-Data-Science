# using loops and functions together

def take_square(x):
    print(x**2)

take_square(2)

salaries = [1000,2000,3000,4000,5000]

for i in salaries:
    print(i)
    
# 20% pay raise 

1000 * 20/100 + 1000
salaries[0] * 20/100 + salaries[0]

def new_salary(l):
    print(l*20/100+l)

new_salary(1000)

for u in salaries:
    new_salary(u)

# alternative but without function
for y in salaries:
    print(y*20/100+y)
    
# another alternative without function
salaries[0]*120/100

for z in salaries:
    print(z*120/100)
    
# pay raise, but user's gonna enter the percentage. again without function.

percentage = int(input("Please enter the pay raise percentage:"))

for t in salaries:
    print(t*(100+percentage)/100)
    
    
# pay raise, but user's gonna enter the percentage. with function.

def new_salary2(t,s):
    print(s*(100+t)/100)
    
t = int(input("Please enter the pay raise percentage:"))
    
for b in salaries:
    new_salary2(t, b)
    
# mini app about if, for and functions
# if the salary is less than 3000 pay raise will be 20% pay raise, if salary is greater then 3000, pay raise will be 10%

salaries = [1000,2000,3000,4000,5000]

def big_salary(x):
    print(x*110/100)

def small_salary(x):
    print(x*120/100)

for i in salaries:
    if i >= 3000:
        big_salary(i)
    else:
        small_salary(i)
        
        
# break & continue

salaries = [8000,5000,2000,1000,3000,7000,1000]
dir(salaries)

salaries.sort()
salaries

for i in salaries:
    if i == 3000:
        print("stopped!")
        break
    print(i)

for i in salaries:
    if i == 3000:
        continue
    print(i)
    
# while

number = 1

while number<10:
    number += 1
    print(number)