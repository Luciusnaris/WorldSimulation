import random

class Citizen:
    def __init__(self, age, money):
        self.age = age
        self.money = money
        self.state = "Alive"
        self.parents = []
        self.children = []
        self.partner = None
        self.pregnancy = 0
        self.housing = True
        self.unpaid_rent=0
        #FOR SEX
        if random.random() < 0.512:
            self.sex = "Male"
        else:
            self.sex = "Female"
        #SALARY PROBABILITY   
        probability = random.randint(1, 10)
        if probability <= 7:
            self.salary = random.randint(30, 60) * 100
        else:
            self.salary = 0
        
        if self.salary > 0:
            self.statut = "Employed"
        else:
            self.statut = "Unemployed"

        if self.age >= 60:
            self.statut = "Retired"
        #HAPPINESS DEPENDANCING ON SALARY
        self.happiness = 00 # Initial happiness value
    
    def age_up(self):
        self.age += 1
        if self.age > 59:
            self.statut = "Retired"
        else:
            pass
