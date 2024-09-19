# object oriented programming 

# Class

# =============================================================================
# class dataScientist():
#     print("This is a class.")
# =============================================================================
    
# class attributes

class dataScientist():
    department = ''
    sql = 'Yes'
    experience_time = 0
    languages = []
    
# access to the class's attributes
dataScientist.department
dataScientist.sql

# changing class's attributes

dataScientist.sql = "No"
dataScientist.sql

# class instantiation

john = dataScientist()
john.sql
john.experience_time
john.department
john.languages.append("Python")
john.languages

steve = dataScientist()
steve.sql
steve.languages

# more about instance

class dataScientist():
    department = ''
    sql = ''
    experience_time = 0
    languages = ["R","Python"]
    def __init__(self):
        self.languages = []
        self.department = ''

john = dataScientist()
john.languages

steve = dataScientist()
steve.languages

john.languages.append("Python")
john.languages

steve.languages
steve.languages.append("R")
steve.languages

dataScientist.languages

john.department
dataScientist.department
john.department = 'statisctics'
dataScientist.department
steve.department = "industrial engineering"
steve.department
john.department


# instance methods

class dataScientist():
    employees = []
    def __init__(self):
        self.languages = []
        self.department = ''
    def add_language(self,new_language):
        self.languages.append(new_language)
        
john = dataScientist()
john.languages
john.department

steve = dataScientist()
steve.languages
steve.department

dir(dataScientist)

dataScientist.add_language("R")
john.add_language("R")
john.languages

steve.add_language("Python")
steve.languages

# inheritance 

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        
class DataScientists(Employees):
    def __init__(self):
        self.Programming = ""

datascientist1 = DataScientists()
datascientist1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
mar1.

# alternative

class Employees2():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        
john = Employees2("a", "b", "c")
john.FirstName
