import random

from rules import death_probability, birth_probability, job_finding, job_losing, income_tax, housing

from citizen import Citizen

citizens = []

month = 0

year = 0


# CREATE INITIAL CITIZENS
for i in range(10):
    citizen = Citizen(random.randint(20, 39), random.randint(1000, 10000))
    citizens.append(citizen)


# LIST OF EVENTS

def death():

    # CITIZEN DYING AND DYING CHANCE
    for citizen in citizens:
        if citizen.state == "Alive":
            death_chance = death_probability(citizen.age)

            if random.random() < death_chance:
                citizen.state = "Dead"
                citizen.money = 0
                citizen.salary = 0
                citizen.happiness = 0

                # REMOVE THE RELATIONSHIP WITH THEIR PARTNER
                if citizen.partner is not None:
                    citizen.partner.partner = None
                    citizen.partner = None


def job():

    # CHECK IF ALIVE CITIZENS FIND A JOB
    for citizen in citizens:
        if citizen.state == "Alive":
            chance = job_finding(citizen.age)

            if random.random() < chance:
                citizen.statut = "Employed"


def losing_job():

    # CHECK IF EMPLOYED CITIZENS LOSE THEIR JOB
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Employed":
            losing_chance = job_losing(citizen.age)

            if random.random() < losing_chance:
                citizen.statut = "Unemployed"


def tax():

    # APPLY INCOME TAX TO EACH ALIVE CITIZEN
    for citizen in citizens:
        if citizen.state == "Alive":
            taxes = income_tax(citizen.salary)
            tax_amount = citizen.salary * taxes

            if citizen.money >= tax_amount:
                citizen.money -= tax_amount
            else:
                citizen.money = 0


def birth():

    # HANDLE EXISTING PREGNANCIES
    # A COPY OF THE LIST IS USED BECAUSE BABIES ARE ADDED TO THE ORIGINAL LIST
    for citizen in citizens[:]:
        if citizen.state == "Alive" and citizen.pregnancy > 0:
            citizen.pregnancy += 1

            # PREGNANCY LASTS 9 MONTHS
            if citizen.pregnancy >= 9:
                baby = Citizen(0, 0)

                # CREATE THE PARENT-CHILD RELATIONSHIP
                citizen.children.append(baby)
                baby.parents.append(citizen)

                citizens.append(baby)
                citizen.pregnancy = 0

    # CHECK IF ALIVE FEMALE CITIZENS CAN BECOME PREGNANT
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.sex == "Female":

            # CITIZEN MUST BE OLD ENOUGH AND HAVE A PARTNER
            if citizen.age >= 12 and citizen.partner is not None:

                # A CITIZEN CANNOT HAVE TWO PREGNANCIES AT THE SAME TIME
                if citizen.pregnancy == 0:
                    chance = birth_probability(citizen.age)

                    # LOW MONEY REDUCES THE CHANCE OF HAVING A CHILD
                    if citizen.money < 1500:
                        chance *= 0.5

                    # HIGH MONEY INCREASES THE CHANCE OF HAVING A CHILD
                    elif citizen.money >= 5000:
                        chance *= 1.25

                    if random.random() < chance:
                        citizen.pregnancy = 1


def find_partners():

    # TEMPORARY LISTS FOR SINGLE MALES AND FEMALES
    single_males = []
    single_females = []

    # FIND ALIVE SINGLE ADULT CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.partner is None and citizen.age >= 18:

            if citizen.sex == "Male":
                single_males.append(citizen)
            else:
                single_females.append(citizen)

    # SHUFFLE BOTH LISTS TO MAKE PARTNERS RANDOM
    random.shuffle(single_males)
    random.shuffle(single_females)

    # PAIR MALES AND FEMALES UNTIL ONE OF THE LISTS IS EMPTY
    for male, female in zip(single_males, single_females):
        male.partner = female
        female.partner = male


def happiness():

    # CALCULATE HAPPINESS FOR EVERY ALIVE CITIZEN
    for citizen in citizens:
        if citizen.state != "Alive":
            continue

        score = 0

        # MONEY: UP TO 35%
        if citizen.money >= 10000:
            score += 35
        else:
            score += (citizen.money / 10000) * 35

        # SALARY: UP TO 30%
        if citizen.salary >= 10000:
            score += 30
        else:
            score += (citizen.salary / 10000) * 30

        # HOUSING: UP TO 20%
        if citizen.housing:
            score += 20

        # PARTNER: +8%
        if citizen.partner is not None:
            score += 8

        # CHILDREN: +5% MAXIMUM
        score += min(len(citizen.children) * 1, 5)

        # HAPPINESS CANNOT EXCEED 98%
        citizen.happiness = min(score, 98)


def advance_time():

    global month
    global year

    # ADVANCE MONTH BY ONE
    month += 1

    # EVERY 12 MONTHS, A NEW YEAR BEGINS
    if month % 12 == 0:
        year += 1

        # REINITIALIZE MONTH TO 0
        month = 0

        # EVERY ALIVE CITIZEN AGES UP EVERY YEAR
        for citizen in citizens:
            if citizen.state == "Alive":
                citizen.age_up()

    # PROCESS MONTHLY ECONOMIC ACTIVITY
    for citizen in citizens:
        if citizen.state == "Alive":

            # CITIZEN RECEIVES THEIR MONTHLY SALARY
            citizen.money += citizen.salary

            # RANDOM FOOD SPENDING BETWEEN 5% AND 10% OF CURRENT MONEY
            food = citizen.money * random.uniform(0.05, 0.1)

            # HOUSING COST
            rent = housing()

            # CHECK IF THE CITIZEN CAN PAY THEIR RENT
            if citizen.money >= rent:
                total_spend = food + rent

                # REMOVE MONTHLY EXPENSES FROM THE CITIZEN'S MONEY
                citizen.money -= total_spend

                # RESET UNPAID RENT BECAUSE THE RENT WAS PAID
                citizen.unpaid_rent = 0

            elif citizen.money < rent:
                # CITIZEN CAN ONLY PAY FOR FOOD
                total_spend = food
                citizen.money -= total_spend

                # COUNT CONSECUTIVE MONTHS WITHOUT PAYING RENT
                citizen.unpaid_rent += 1

                # AFTER 3 MONTHS WITHOUT PAYING RENT, THE CITIZEN LOSES THEIR HOUSING
                if citizen.unpaid_rent == 3:
                    citizen.housing = False

    # PROCESS ALL MONTHLY EVENTS
    death()
    job()
    losing_job()
    tax()
    find_partners()
    birth()
    happiness()


def population_stats_details():

    alive_count = 0
    dead_count = 0
    employed_count = 0
    unemployed_count = 0
    retired_count = 0
    homeless_count = 0

    # COUNT ALIVE AND DEAD CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive":
            alive_count += 1
        else:
            dead_count += 1

    # CALCULATE AVERAGE AGE
    total_age = 0

    for citizen in citizens:
        if citizen.state == "Alive":
            total_age += citizen.age

    try:
        average_age = total_age / alive_count

    except ZeroDivisionError:
        average_age = 0
        print("Every citizen is dead.")

    # CALCULATE AVERAGE SALARY
    total_salary = 0

    # COUNT EMPLOYED CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Employed":
            employed_count += 1

    # ADD THE SALARY OF WORKING-AGE CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.age < 60:
            total_salary += citizen.salary

    # AVERAGE SALARY CALCULATION
    try:
        average_salary = total_salary / employed_count

    except ZeroDivisionError:
        average_salary = 0
        print("Every citizen is dead.")

    # EMPLOYMENT RATE
    try:
        employment_rate = employed_count / alive_count * 100

    except ZeroDivisionError:
        employment_rate = 0

    # COUNT UNEMPLOYED CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Unemployed":
            unemployed_count += 1

    # UNEMPLOYMENT RATE
    try:
        unemployment_rate = unemployed_count / alive_count * 100

    except ZeroDivisionError:
        unemployment_rate = 0

    # COUNT RETIRED CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.statut == "Retired":
            retired_count += 1

    # RETIREMENT RATE
    try:
        retirement_rate = retired_count / alive_count * 100

    except ZeroDivisionError:
        retirement_rate = 0

    # COUNT HOMELESS CITIZENS
    for citizen in citizens:
        if citizen.state == "Alive" and citizen.housing == False:
            homeless_count += 1

        try:
            homeless_rate = homeless_count / alive_count * 100

        except ZeroDivisionError:
            homeless_rate = 0

    senior_count = 0
    major_count = 0
    minor_count = 0

    # COUNT SENIORS, ADULTS AND MINORS
    for citizen in citizens:
        if citizen.state == "Alive":

            if citizen.age >= 60:
                senior_count += 1

            elif citizen.age >= 18:
                major_count += 1

            else:
                minor_count += 1

    # RETURN ALL CALCULATED STATISTICS
    return alive_count, dead_count, average_age, employment_rate, unemployment_rate, retirement_rate, average_salary, senior_count, major_count, minor_count, homeless_rate


def population_info():

    # GET ALL POPULATION STATISTICS
    stats = population_stats_details()

    # DISPLAY THE MAIN POPULATION INFORMATION
    print(f"""=== WORLD-SIMULATION ===
Population: {stats[0]}
Dead: {stats[1]}
Average Age: {stats[2]:.2f}
Employment: {stats[3]:.2f}%
Unemployment: {stats[4]:.2f}%
Retirement: {stats[5]:.2f}%
Homeless: {stats[10]:.2f}%

Press [D] for details

""")