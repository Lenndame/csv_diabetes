"""
Lese die Datei diabetes2.csv mit Hilfe der csv-Library ein.
Auf Basis dieser Datei soll eine neue Datei erstellt werden, die nur
die Spalten BMI, age und outcome berücksichtigt.
Ferner sollen nur Einträge berücksichtigt werden
mit outcome = 1

Schreibe die Daten kommasepariert in eine neue Datei:
diabetes_positive_outcome.csv

Außerdem interessieren uns folgende Werte, die am Ende des Schreibvorgangs
noch ausgegeben werden sollen:

Für alle Einträge mit outcome=1
Mittelwert BMI
Mittelwert Alter
Median BMI
Median Alter
Max BMI, Min BMI
MAX BloodPRESSURE

für Median und Mittelwert nutze das statistics Modul
import statistics
median = statistics.median([2, 3, 4, 5])
mean = statistics.mean([2, 3, 4, 5])

für min/max nutze die Builtin-Funktionen min([1, 2, 3])
und max([3, 2, 1])

"""
import csv
import statistics
from pathlib import Path


blood_list = []
diabetes_list = []
with open(Path(__file__).parent / "diabetes2.csv") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        if row["Outcome"] == "1":
            blood = {"BloodPressure":row["BloodPressure"]}
            blood_list.append(blood)
            dic = {"BMI": row["BMI"], "Age": row["Age"], "Outcome": row["Outcome"]}
            diabetes_list.append(dic)
            
with open(Path(__file__).parent / "diabetes_positiv_outcome.csv", mode="w", newline="") as f:
    fieldnames = ["BMI", "Age", "Outcome"]
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
    writer.writeheader()
    writer.writerows(diabetes_list)

median_bmi = statistics.median(float(d["BMI"]) for d in diabetes_list)
median_age = statistics.median(int(d["Age"]) for d in diabetes_list)
mw_bmi = statistics.mean(float(d["BMI"]) for d in diabetes_list)
mw_age = statistics.mean(int(d["Age"]) for d in diabetes_list)
max_bmi = max(float(d["BMI"]) for d in diabetes_list)
min_bmi = min(float(d["BMI"]) for d in diabetes_list)
max_blood = max(int(d["BloodPressure"]) for d in blood_list)

print(f"    Median Alter: {median_age},     Median BMI: {median_bmi},\n\
Mittelwert Alter: {mw_age:.1f}, Mittelwert BMI: {mw_bmi:.1f}\n\
   unterster BMI: {min_bmi},    oberster BMI: {max_bmi}")
print(f"               Höchster Wert Blutdruck: {max_blood}")
