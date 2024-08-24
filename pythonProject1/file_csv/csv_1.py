import csv

with open('baso.csv','r') as file:
    with_open = csv.reader(file)
    for lam in with_open:
        print(lam)