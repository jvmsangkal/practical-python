# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    p = payment
    if months >=  extra_payment_start_month and months < extra_payment_end_month:
        p += extra_payment

    to_be_paid = principal * (1+rate/12)
    if p > to_be_paid:
        p = to_be_paid

    principal = to_be_paid - p
    total_paid = total_paid + p
    print(months, round(total_paid, 2), round(principal, 2))
    months += 1
