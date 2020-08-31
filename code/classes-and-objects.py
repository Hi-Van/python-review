#defining a class and object
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

#using a class
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

Alex = student("Alex", "Computer Science", 3.1)

#defining class functions
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

Alex = student("Alex", "Computer Science", 3.1)

print(Alex.on_honor_roll())

#inheriting class information
class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

class alumni(student):
    def is_attending(self):
        return False

Alex = alumni("Alex", "Computer Science", 3.1)

print(Alex.is_attending())        