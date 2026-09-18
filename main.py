import random

citizens = [] 

month = 0

def create_name():
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    return random.choice(names)

def create_money():
    return random.randint(100, 5000)

def create_age():
    return random.randint(20, 39)

def create_citizen():
    citizen = {
        "name": create_name(),
        "money": create_money(),
        "age": create_age()
    }
    citizens.append(citizen)
    print(f"""Citizen added!
Name: {citizen['name']}
Age: {citizen['age']}
Money: {citizen['money']}""")

def aging():     
    for citizen in citizens:
        citizen["age"] += 1

def advance_time():
    global month
    month += 1
    if month % 12 == 0:
        aging()

def display_citizens():
    for citizen in citizens:
        print(f"Name: {citizen['name']}, Money: {citizen['money']}, Age: {citizen['age']}")
        
def menu():
    print(f"""===== WORLD SIMULATION =====
Month : {month}

1. Advance time
2. Add citizen
3. Display citizens
4. Exit
============================""")
    choice = input("Enter your choice: ")
    if choice == "1":
        advance_time()
    elif choice == "2":
        create_citizen()
    elif choice == "3":
        display_citizens()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")
while True:
    menu()  