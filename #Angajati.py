import random

class Angajat:
    def __init__(self, nume: str, ore_pe_luna: int) -> None:
        self.Nume = nume
        self.Ore_pe_luna = ore_pe_luna
        self.Ore_pe_saptamana = ore_pe_luna // 4
        self.Zile_lucrate = []  # List to store the days the employee is working
        self.worked_hours = 0

    def add(self):
        return {
            "Nume": self.Nume,
            "Ore_pe_saptamana": self.Ore_pe_saptamana,
            "Ore_pe_luna": self.Ore_pe_luna,
            "Zile_lucrate": self.Zile_lucrate,
            "Ore_lucrate": self.worked_hours
        }

def add_to_schedule(Anagajati, Saptamana):
    days_of_week = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
    
    for day in days_of_week:
        workers_needed = random.randint(3, 6)  # Workers needed for the day
        
        available_workers = [angajat for angajat in Anagajati.values() if angajat["Ore_pe_saptamana"] > 0 and len(angajat["Zile_lucrate"]) <= 5]
        available_workers = sorted(available_workers, key=lambda x: x["Ore_pe_saptamana"], reverse=True)
        
        assigned_workers = 0
        while available_workers and sum(worker['Ore_pe_saptamana'] for worker in available_workers) > 0:
            angajat = available_workers.pop(0)
            remaining_hours = angajat["Ore_pe_saptamana"]
            max_hours = min(8, remaining_hours)  # Maximum hours an employee can work on a day
            
            available_hours = max_hours if Saptamana[day]["hours"] + max_hours <= Num_Angajati*5 else min(1, angajat['Ore_pe_saptamana'] - Saptamana[day]["hours"])#Are legatura cu numarul de angajati si nr ala 28!!
            
            if available_hours > 0:
                Saptamana[day]["hours"] += available_hours
                angajat['Ore_lucrate'] += available_hours
                angajat["Ore_pe_saptamana"] -= available_hours
                angajat["Ore_pe_luna"] -= available_hours
                angajat["Zile_lucrate"].append(day)  # Update the days worked for the employee
                assigned_workers += 1
                Saptamana[day]["workers"].append(angajat["Nume"])  # Add the employee to the list of workers for the day
            else:
                break
            
        if sum(worker['Ore_pe_saptamana'] for worker in available_workers) > 0:
            while available_workers and Saptamana[day]["hours"] < 12:
                angajat = available_workers.pop(0)
                remaining_hours = angajat["Ore_pe_saptamana"]
                max_hours = min(8, remaining_hours)
                
                available_hours = min(max_hours, 12 - Saptamana[day]["hours"])
                
                if available_hours > 0:
                    Saptamana[day]["hours"] += available_hours
                    angajat['Ore_lucrate'] += available_hours
                    angajat["Ore_pe_saptamana"] -= available_hours
                    angajat["Ore_pe_luna"] -= available_hours
                    angajat["Zile_lucrate"].append(day)
                    Saptamana[day]["workers"].append(angajat["Nume"])
        
    remaining_hours = sum(angajat["Ore_pe_saptamana"] for angajat in Anagajati.values())
    if remaining_hours == 0:
        print("Complete")
    else:
        print("Incomplete")


def get_employee_hours_summary(Anagajati):
    total_employees = len(Anagajati)
    total_hours = sum(angajat["Ore_pe_saptamana"] for angajat in Anagajati.values())
    return total_employees, total_hours



# Example usage:
Anagajati = {}

Saptamana = {
    "Luni": {"hours": 0, "workers": []},
    "Marti": {"hours": 0, "workers": []},
    "Miercuri": {"hours": 0, "workers": []},
    "Joi": {"hours": 0, "workers": []},
    "Vineri": {"hours": 0, "workers": []},
    "Sambata": {"hours": 0, "workers": []},
    "Duminica": {"hours": 0, "workers": []}
}





Andrei = Angajat("Andrei", 160)
Anagajati["Andrei"] = Andrei.add()
Andrei1=Angajat("Andrei1", 80)
Anagajati["Andrei1"]=Andrei1.add()
Andrei2=Angajat("Andrei2", 140)
Anagajati["Andrei2"]=Andrei2.add()
Andrei3=Angajat("Andrei3", 120)
Anagajati["Andrei3"]=Andrei3.add()
Andrei4=Angajat("Andrei4", 120)
Anagajati["Andrei4"]=Andrei4.add()
Andrei5=Angajat("Andrei5", 120)
Anagajati["Andrei5"]=Andrei5.add()
Andrei6=Angajat("Andrei6", 80)
Anagajati["Andrei6"]=Andrei6.add()
Andrei7=Angajat("Andrei7", 80)
Anagajati["Andrei7"]=Andrei7.add()
Andrei8=Angajat("Andrei8", 160)
Anagajati["Andrei8"]=Andrei8.add()
Andrei9=Angajat("Andrei9", 160)
Anagajati["Andrei9"]=Andrei9.add()

Num_Angajati, Total_weekly_hours=get_employee_hours_summary(Anagajati)
print(get_employee_hours_summary(Anagajati))

add_to_schedule(Anagajati, Saptamana)


# Display the updated schedule and employee working hours
print("Updated Saptamanal:")
#print(Saptamana)


for angajat in Anagajati.values():
    print(f"Nume: {angajat['Nume']}, Ore pe saptamana: {angajat['Ore_pe_saptamana']}, Ore pe luna: {angajat['Ore_pe_luna']}, Zile lucrate: {angajat['Zile_lucrate']}, Ore lucrate: {angajat['Ore_lucrate']}")


for days in Saptamana.values():
    print(f"{days}")

