
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

def job_finding(age):
    if 18<= age <=24:
        return 0.03 
    elif 25<= age <= 34:
        return 0.05
    elif 35<= age <= 44:
        return 0.05
    elif 45<= age <= 54:
        return 0.04
    elif 55<= age <= 59:
        return 0.03
    elif age > 59:
        return 0
    
def job_losing(age):
    if 18<= age <= 24:
        return 0.03
    elif 25<= age <= 34:
        return 0.02
    elif 35 <= age <= 44:
        return 0.02
    elif 45<= age <= 54:
        return 0.02
    elif 55<= age <= 59:
        return 0.025
    elif age > 59:
        return 0
    
def birth_probability(age):
    if age < 6:
        return 0.00
    elif age < 14:
        return 0.0010
