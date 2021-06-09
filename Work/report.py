# report.py
#
# Exercise 2.4

import csv

# def portfolio_cost(filename):

#     total_cost = 0

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#     return total_cost

def read_portfolio(filename):
    # portfolio = []

    # with open(filename, 'rt') as file:
    #     rows = csv.reader(file)
    #     headers = next(rows)
    #     for row in rows:
    #         holding = row[0], int(row[1]), float(row[2])
    #         portfolio.append(holding)
    #     # for name, shares, price in rows:
    #     #     print(name, shares, price)
    
    # return portfolio

    portfolio = []

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            stock = {}
            name, shares, price = row
            stock['name'] = name
            stock['shares'] = int(shares)
            stock['price'] = float(price)
            portfolio.append(stock)

    return portfolio

