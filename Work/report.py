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

# { name: func(val) for name, func, val in zip(headers, types, row) }
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            stock = {
                # 'name':row[0],
                'name' : record['name'],
                # 'shares':int(row[1]),
                'shares':int(record['shares']),
                # 'price':float(row[2])
                'price':float(record['price'])
            }
            


            # name, shares, price = row
            # stock['name'] = name
            # stock['shares'] = int(shares)
            # stock['price'] = float(price)
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    
    prices = {}

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        # headers = next(rows)

        for row in rows:
            if len(row) != 0:
            #     print(row)
            # else:
                prices[row[0]] = float(row[1])

    return prices

def make_report(portfolio, prices):
    report = []
    
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = stock['price'] - current_price
        summary = (stock['name'], stock['shares'], current_price, change)
        report.append(summary)

    
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')


# Calculate the total cost of the portfolio
total_cost = 0.0
for stocks in portfolio:
    total_cost += stocks['shares']*stocks['price']

# print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for stocks in portfolio:
    # print(s)
    total_value += stocks['shares']*prices[stocks['name']]

# print(prices)
# print('Current value', total_value)
# print('Gain', total_value - total_cost)
