# pcost.py
#
# Exercise 1.27

# def portfolio_cost(filename):
#     total = 0
#     file = open(filename, 'rt')
#     headers = next(file).split(',')

#     for line in file:
#         row = line.split(',')
#         # numberofstocks = float(row[1])
#         # priceofstock = float(row[2])
#         # sumofstock = numberofstocks * priceofstock
#         # total = total + sumofstock
#         total += float(row[1]) * float(row[2])
#     return total

# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost', cost)

import csv
def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except ValueError:
                print('Bad row:', row)
        
    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
