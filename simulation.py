import random
from rules import death_probability, birth_probability, job_finding, job_losing
from citizen import Citizen

citizens = []

month = 0
year = 0


for i in range(10):
    citizen = Citizen(random.randint(20, 39), random.randint(1000, 10000))
    citizens.append(citizen)

#LIST OF EVENT

def death():
#CITIZEN DYING AND DYING CHANCE
    for citizen in citizens:
        if citizen.state == "Alive":
            death_chance = death_probability(citizen.age)

            if random.random() < death_chance:
                citizen.state = "Dead"
                citizen.money = 0
                citizen.salary = 0
                citizen.happiness = 0 

def job():
    for citizen in citizens:
        if citizen.state == "Alive":
            chance = job_finding(citizen.age)
            if random.random() < chance:
                citizen.statut = "Employed"

def losing_job():
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Employed":
            losing_chance = job_losing(citizen.age)
            if random.random()<losing_chance:
                citizen.statut = "Unemployed"

def birth():
    #I REALLY DON'T KNOW HOW
    pass

def advance_time():
    global month
    global year
    month += 1#ADVANCE MONTH BY ONE
    if month % 12 == 0:
        year += 1#YEARS BY ONE
        month = 0#REINITIALIZE MONTH TO 0
        for citizen in citizens:
            if citizen.state == "Alive":    
                citizen.age_up()  # every citizen ages up every year
    for citizen in citizens:
        if citizen.state == "Alive":
            citizen.money += citizen.salary
            spend = citizen.money * random.uniform(0.1, 0.5)  # Random spending between 10% and 50%
            citizen.money -= spend# this is the amount of money spent by the citizen each month, which is a random percentage of their current money
    death()  # If the citizen is dead, we don't need to do anything
    job()
    losing_job()

def population_stats_details():
    alive_count = 0
    dead_count = 0
    employed_count = 0
    unemployed_count = 0
    retired_count = 0
    #Alive and Dead count
    for citizen in citizens:
        if citizen.state == "Alive":
            alive_count += 1
        else:
            dead_count += 1
    #Average Age      
    total_age = 0
    for citizen in citizens:
        if citizen.state == "Alive":
            total_age += citizen.age
    try:
        average_age = total_age / alive_count
    except ZeroDivisionError:
        average_age = 0
        print("Every citizen is dead.")
    #AVERAGE SALARY
    total_salary = 0
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Employed":#CHECK IF EMPLOYED
            employed_count += 1
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.age < 60:
            total_salary += citizen.salary
    #AVERAGE SALARY CALCUL
    try:
        average_salary = total_salary / employed_count
    except ZeroDivisionError:
        average_salary = 0
        print("Every citizen is dead.")
    #EMPLOYMENT RATE
    try:
        employment_rate = employed_count / alive_count * 100
    except ZeroDivisionError:
        employment_rate = 0#(I DIDN'T MAKE ANOTHER LOOP WHO CHECK EMPLOYMENT AND ALIVE PEOPLE CAUSE IT WOULD MAKES MY CALCUL FALSE)
    #AND HERE I MADE ONE CAUSE I DIDN'T MADE A COUNT OF UNEMPLOYMENT
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Unemployed":
            unemployed_count +=1
    try:
        unemployment_rate = unemployed_count / alive_count * 100
    except ZeroDivisionError:
        unemployment_rate = 0
    #SAME HERE
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Retired":
            retired_count += 1
    try:
        retirement_rate = retired_count / alive_count * 100
    except ZeroDivisionError:
        retirement_rate = 0
    senior_count = 0
    major_count = 0
    minor_count = 0
#AND HERE I DISPLAY STATS
    for citizen in citizens:
        if citizen.state == "Alive":
            if citizen.age >= 60:
                senior_count += 1
            elif citizen.age >= 18:
                major_count += 1
            else:
                minor_count += 1
    return alive_count, dead_count, average_age, employment_rate, unemployment_rate, retirement_rate, average_salary, senior_count, major_count, minor_count
     
def population_info():
    stats = population_stats_details()

    print(f"""=== WORLD-SIMULATION ===
Population: {stats[0]}
Dead: {stats[1]}
Average Age: {stats[2]:.2f}
Employment: {stats[3]:.2f}%
Unemployment: {stats[4]:.2f}%
Retirement: {stats[5]:.2f}%
Press [D] for details
""")