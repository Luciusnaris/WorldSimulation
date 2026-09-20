import random

citizens = []

class Citizen:
    def __init__(self, age, money):
        self.age = age
        self.money = money
        
for i in range(100):
    citizen = Citizen(random.randint(20, 39), random.randint(1000, 10000))
    citizens.append(citizen)
    print(f"Citizen {i+1}: Age: {citizen.age}, Money: {citizen.money}")
        
