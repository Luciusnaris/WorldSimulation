import simulation
import keyboard


       
def display_citizens():
    print(f"Year: {simulation.year}, Month: {simulation.month}")
    for i in range(len(simulation.citizens)):
        citizen = simulation.citizens[i]
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

def display_date():
    print(f"\nYear: {simulation.year} ¦ Month: {simulation.month}\n")

print("Initial citizens:")
display_citizens()
while True:
    if keyboard.is_pressed('1'):
        simulation.advance_time()
        display_date()
        simulation.population_info()
        while keyboard.is_pressed('1'):
            pass  # Wait until the key is released

    elif keyboard.is_pressed('2'):
        for _ in range(3):
            simulation.advance_time()
        display_date()
        simulation.population_info()
        while keyboard.is_pressed('2'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('shift'):
        for _ in range(12):
            simulation.advance_time()
        display_date()
        simulation.population_info()
        while keyboard.is_pressed('shift'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('tab'):
        for _ in range(36):
            simulation.advance_time()
        display_date()
        simulation.population_info()
        while keyboard.is_pressed('tab'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('j'):
        display_citizens()
        while keyboard.is_pressed('j'):
            pass  # Wait until the key is released
    elif keyboard.is_pressed('d'):
        stats = simulation.population_stats_details()
        print(f"\nPopulation Statistics:\nAlive: {stats[0]}\nDead: {stats[1]}\nAverage Age: {stats[2]:.2f}\nEmployment Rate: {stats[3]}\nUnemployment Rate: {stats[4]}\nRetirment Rate: {stats[5]}\nHomeless Rate: {stats[10]}\nAverage Salary: ${stats[6]:,.2f}\nSeniors (60+): {stats[7]}\nAdults (18-59): {stats[8]}\nMinors (<18): {stats[9]}")
        while keyboard.is_pressed('d'):
            pass
    elif keyboard.is_pressed('end'):
        break