import random

citizens = [] 

def create_name():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    return random.choice(names)

name = create_name()

def create_money():
    return random.randint(100, 5000)

money = create_money()

def create_citizen():
    citizen = {
        "name": name,
        "money": money
    }
    citizens.append(citizen)
