# Data Structures - Lists

# []
# list()

grades = [90,80,70,50]
type(grades)

list1 = ["a",19.3,90]

list2 = ["a",19.3,90, grades]

len(list2)

type(list2[0])

all_lists = [list1,list2]

del all_lists


# more about lists

listt = [10,20,30,40,50]
listt[1]
listt[6]
listt[0:2]
listt[2:]

new_list = ["a",10,[20,30,40,50]]

new_list[0:2]

new_list[2][1]

# Lists - Item Changings

list3 = ["john","justin","stacy","robin"]
list3[1] = "justins_father"
list3[1]= "justin"

list3[0:3] = "jhons_papa","justins_father","stacys_father"
list3

list3 = ["john","justin","stacy","robin"]
list3

list3 = list3 + ["mark"]
list3

del list3[3]
list3

# Lists - List Methods

list4 = ["john","justin","stacy"]
dir(list4)

# append & remove

list4.append("jason")
list4

list4.remove("jason")
list4

# insert 

list5 = ["john","justin","stacy"]

list5.insert(0, "robin")
list5

list5.insert(2, "bob")
list5
list5.insert(5, "jake")
list5
len(list5)
list5.insert(len(list5), "emma")
list5

# pop 

list5.pop(0)
list5
list5.pop(4)
list5

# count

list6 = ["john","justin","stacy","john","justin"]
list6.count("john")
list6.count("justin")
list6.count("stacy")

# copy

list6_backup = list6.copy()

# extend

list6.extend(["a","b",10])
list6

# index

list6.index("john")

# reverse

list6.reverse()
list6

# sort
list6 = [10,40,5,90]
list6.sort()
list6

# clear

list6.clear()
list6

