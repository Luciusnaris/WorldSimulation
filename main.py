import random
import keyboard


citizens = []

month = 0
year = 0

class Citizen:
    def __init__(self, age, money):
        self.age = age
        self.money = money
        probability = random.randint(1, 10)
        if probability <= 7:
            self.salary = random.randint(30, 60) * 100
        else:
            self.salary = 0

    def age_up(self):
        self.age += 1

#FONCTION HORS CLASSE
def advance_time():
    global month
    global year
    month += 1
    if month % 12 == 0:
        year += 1
        month = 0
        for citizen in citizens:    
            citizen.age_up()#every citizen ages up every year
    for citizen in citizens:
        citizen.money += citizen.salary
        spend = citizen.money * random.uniform(0.1, 0.5)  # Random spending between 10% and 50%
        citizen.money -= spend# this is the amount of money spent by the citizen each month, which is a random percentage of their current money


print("Initial citizens:")
print(f"Year: {year}, Month: {month}") 
for i in range(10):
    citizen = Citizen(random.randint(20, 39), random.randint(1000, 10000))
    citizens.append(citizen)
    if citizen.salary > 0:
        statut = "Employed"
    else:
        statut = "Unemployed"     
    if citizen.age >= 60:
        statut = "Retired"
        citizen.salary = 0
        
def display_citizens():  
    for i in range(len(citizens)):
        citizen = citizens[i]
        if citizen.salary > 0:
            statut = "Employed"
        else:
            statut = "Unemployed"     
        if citizen.age >= 60:
            statut = "Retired"
            citizen.salary = 0  
        if statut == "Employed":
            print(f"Citizen {i+1}: Age: {citizen.age}, Money: {citizen.money}, Status: {statut}, Salary: {citizen.salary}")
        else:
            print(f"Citizen {i+1}: Age: {citizen.age}, Money: {citizen.money}, Status: {statut}")

display_citizens()
while True:
    if keyboard.is_pressed('1'):
        advance_time()
        display_citizens()

    elif keyboard.is_pressed('2'):
        for _ in range(3):
            advance_time()
        display_citizens()
    elif keyboard.is_pressed('shift'):
        for _ in range(12):
            advance_time()
        display_citizens()
    elif keyboard.is_pressed('tab'):
        for _ in range(36):
            advance_time()
        display_citizens()