import random
import time
import keyboard

speed = 0.5  # Adjust the speed of the simulation
paused = False  # Variable to track the pause state

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
            citizen.age_up()
    for citizen in citizens:
        citizen.money += citizen.salary
        spend = citizen.money * random.uniform(0.1, 0.5)  # Random spending between 10% and 50%
    
    
print("""
===== WORLD SIMULATION =====

1 → Normal speed
2 → Fast speed
3 → Slow speed
0 → Pause

""")

for seconds in range(10, 0, -1):
    print(f"\rThe simulation will start in {seconds} seconds...", end="")
    time.sleep(1)
    print("\rThe simulation is starting...          ")       

while True:
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
        
    if statut == "Employed":
        print(f"Citizen {i+1}: Age: {citizen.age}, Money: {citizen.money}, Status: {statut}, Salary: {citizen.salary}")
    else:
        print(f"Citizen {i+1}: Age: {citizen.age}, Money: {citizen.money}, Status: {statut}")
        
    if keyboard.is_pressed('1'):
       speed = 0.5  # Normal speed
       paused = False  # Resume the simulation
       
    elif keyboard.is_pressed('2'):
        speed = 0.1  # Fast speed
        paused = False  # Resume the simulation
        
    elif keyboard.is_pressed('3'):
        speed = 1.0  # Slow speed
        paused = False  # Resume the simulation
        
    elif keyboard.is_pressed('0'):
        paused = True  # Pause the simulation
    
    if not paused:
        advance_time()
        time.sleep(speed)  # Adjust the speed of the simulation based on the speed variable