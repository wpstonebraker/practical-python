# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as file:
        rows = csv.reader(file)

        # Read the file headers
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select] # search for index of colname in headers
            headers = select
        else:
            indices = [] # if blank it'll skip conditional in loop below

        
        records = []
        for row in rows:
            if not row: # skips row with no data
                continue
            if indices: # if indices isn't blank, replace row with new row of relevant data
                row = [row[index] for index in indices]
            record = dict(zip(headers, row))
            records.append(record)

    return records