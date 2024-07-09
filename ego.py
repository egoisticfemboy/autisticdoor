import csv

f = "Wetterdaten24.06.2024-30.06.2024.csv"
# f as abbreviation for file
data = []

with open (f, mode='r') as file:
    
    re = csv.reader(file, delimiter=';')
    #re as abbreviation for reader
    
    he = next(re)
    # he as abbreviation for header
    
    for row in re:
        data.append(row)
        

print(data)
