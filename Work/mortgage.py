# mortgage.py
#
# Exercise 1.7

principal = 500000.0 # total loan
rate = 0.05 # interest
payment = 2684.11 # monthly payment
total_paid = 0.0 # total amount paid
months = 0 # counter for months
extra_payment_start_month = int(input('Extra Payment Start '))
extra_payment_end_month = int(input('Extra Payment End '))
extra_payment = int(input('Amount '))

while principal > 0:
    months += 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment   
    print(months, round(total_paid, 2), round(principal, 2))

# print('Total paid', round(total_paid, 2))
# print('Months', months)

