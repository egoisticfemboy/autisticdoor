# Just a coooler looking version because why not :3
import csv

f = "Wetterdaten24.06.2024-30.06.2024.csv"
d = []

try:
    with open(f, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        d = list(reader)
except FileNotFoundError:
    print(f"The file {f} could not be found. Please check the file name and if it exist")
except csv.Error as e:
    print(f"Error at reading the CSV file: {e}")

print(d)
