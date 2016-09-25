class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
        
    def display(self):
        print("Your a ", self.gender, ", and your name is:", self.name)
        #print(value)
people = Person('Male', 'Alex')
people2 = Person('Female','Joan')
people.display()
people2.display()
