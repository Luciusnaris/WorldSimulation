import random
import keyboard


citizens = []

month = 0
year = 0

class Citizen:
    def __init__(self, age, money):
        self.age = age
        self.money = money
        self.state = "Alive"
        probability = random.randint(1, 10)
        if probability <= 7:
            self.salary = random.randint(300, 600) * 100
        else:
            self.salary = 0
        self.happiness = 00 # Initial happiness value
        if self.salary >= 10000:
            self.happiness = 110
        elif self.salary >= 3000:
            self.happiness += 50
        elif self.salary >= 0:
            self.happiness += 30

    def age_up(self):
        self.age += 1

#FONCTION HORS CLASSE

def death_probability(age):
    if age < 5:
        return 0.000418
    elif age < 15:
        return 0.0000834
    elif age < 30:
        return 0.0000834
    elif age < 50:
        return 0.000125
    elif age < 65:
        return 0.000418
    elif age < 75:
        return 0.00126
    elif age < 85:
        return 0.00340
    elif age < 95:
        return 0.00874
    else:
        return 0.0184
    
def death():
    for citizen in citizens:
        if citizen.state == "Alive":
            death_chance = death_probability(citizen.age)

            if random.random() < death_chance:
                citizen.state = "Dead"
                citizen.money = 0
                citizen.salary = 0
                citizen.happiness = 0 

def advance_time():
    global month
    global year
    month += 1
    if month % 12 == 0:
        year += 1
        month = 0
        for citizen in citizens:
            if citizen.state == "Alive":    
                citizen.age_up()  # every citizen ages up every year
    if citizen.state == "Alive":
        for citizen in citizens:
            citizen.money += citizen.salary
            spend = citizen.money * random.uniform(0.1, 0.5)  # Random spending between 10% and 50%
            citizen.money -= spend# this is the amount of money spent by the citizen each month, which is a random percentage of their current money
            death_probability(citizen.age)
    death()  # If the citizen is dead, we don't need to do anything

print("Initial citizens:")
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
    print(f"\nYear: {year}, Month: {month}\n")
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
            print(f"Citizen {i+1} ¦ {citizen.age} ¦ {citizen.state} ¦ Happiness: {citizen.happiness} ¦ ${citizen.money:,.0f} ¦ {statut} ¦ Salary: {citizen.salary:,.0f}")
        else:
            print(f"Citizen {i+1} ¦ {citizen.age} ¦ {citizen.state} ¦ Happiness: {citizen.happiness} ¦ ${citizen.money:,.0f} ¦ {statut} ¦ Salary: {citizen.salary:,.0f}")

display_citizens()
while True:
    if keyboard.is_pressed('1'):
        advance_time()
        display_citizens()
        while keyboard.is_pressed('1'):
            pass  # Wait until the key is released

    elif keyboard.is_pressed('2'):
        for _ in range(3):
            advance_time()
        display_citizens()
        while keyboard.is_pressed('2'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('shift'):
        for _ in range(12):
            advance_time()
        display_citizens()
        while keyboard.is_pressed('shift'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('tab'):
        for _ in range(36):
            advance_time()
        display_citizens()
        while keyboard.is_pressed('tab'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('end'):
        break