# Data Structures - Tuple
# tuples are ordered, just like lists 
# the difference between tuple and list is tuples' items can't be changed.


t = ("john","bob",1,2,3.2,[1,2,3,4])

t = "john","bob",1,2,3.2, [1,2,3,4]

# tuple()

t = ("item",) # when creating a tuple with one item, we should use comma at the end.
type(t)



# tuple item operations

t = ("john","bob",1,2,3.2,[1,2,3,4])
t
t[1]
t[0:3]

t[2] = 99


# Data Structures - Dictionary
# dictionaries are unordered, but its items can be changed. 

dictionary = {"REG" : "Regression Model",
              "LOG" : "Logistic Regression",
              "CART" : "Classification and Regression"}
dictionary

len(dictionary)

dictionary = {"REG" : 10,
              "LOG" : 20,
              "CART" : 30}
dictionary

dictionary = {"REG" : ["RMSE",10],
              "LOG" : ["MSE",20],
              "CART" : ["SSE",30]}
dictionary

# Dictionary Item Operations

dictionary = {"REG" : "Regression Model",
              "LOG" : "Logistic Regression",
              "CART" : "Classification and Regression"}
dictionary[0]
dictionary["REG"]
dictionary["LOG"]

dictionary = {"REG" : ["RMSE",10],
              "LOG" : ["MSE",20],
              "CART" : ["SSE",30]}
dictionary["REG"]

dictionary = {"REG" : {"RMSE" : 10,
                       "MSE" : 20,
                       "SSE" : 30},
              "LOG" : {"RMSE" : 10,
                                     "MSE" : 20,
                                     "SSE" : 30},
              "CART" : {"RMSE" : 10,
                                     "MSE" : 20,
                                     "SSE" : 30}}
dictionary
dictionary["REG"]
dictionary["REG"]["SSE"]

# Dictionary - Item Adding & Changing

dictionary = {"REG" : "Regression Model",
              "LOG" : "Logistic Regression",
              "CART" : "Classification and Regression"}
dictionary["GBM"] = "Gradient Boosting Machine"
dictionary

dictionary["REG"] = "Multiple Linear Regression"
dictionary

dictionary[1] = "Artificial Neural Networks"
dictionary

l = [1]
l
dictionary[l] = "a new thing"

t = ("tuple",)

dictionary[t] = "a new thing"
dictionary

# Data Structures - Sets
# Sets are unordered, has unique values, can be changed.

s = set()
s

l = [1,"a","adien",123]
s = set(l)
s

t = ("a","adien")
s = set(t)
s

adien = "pls_go_to_the_moon"
type(adien)

s = set(adien)
s

l = ["adien","pls","go","to","the","moon"]
l

s = set(l)
s

len(s)

l[0]

s[0] # gives error, because sets are unordered

# Operations in Sets

l = ["adien","moon"]

s = set(l)
s

dir(s)

s.add("with")
s

s.add("to_the_moon")
s

s.add("with")
s

s.remove("adien")
s

s.discard("adien")

# Sets - Difference & Symmetric Difference

# difference() - the difference between two sets
# intersection() - '&' intersection of two sets
# union() - union of two sets
# symmetric_difference() - things that any of the sets have

# difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # items that set1 has but set2 does not have 

set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2

# intersection and union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)

intersection = set1 & set2
intersection

union = set1.union(set2)
union

set1.intersection_update(set2)
set1

# more operations on sets

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# if two sets does not have intersection returns true

set1.isdisjoint(set2)

# if set1 is set2's subset returns true

set1.issubset(set2)

# if set2 encapsulates set1 returns true

set2.issuperset(set1)


