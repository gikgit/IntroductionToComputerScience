outstanding_balance = float(raw_input('the outstanding balance on the credit cart: '))
annual_interest = float(raw_input('annual interest rate: '))

mini_monthly_payment = 0
total_months = 0
remaining_balance = 0
monthly_interesr_rate = annual_interest / 12
flag = 0

while True:
    count = 1
    balance = outstanding_balance
    while count <= 12:
        balance = balance * (1 + monthly_interesr_rate) - mini_monthly_payment
        count = count + 1
        if balance <= 0:
            remaining_balance = balance
            total_months = count - 1
            flag = 1
            break
    if flag == 1:
        break
    else: 
        mini_monthly_payment = mini_monthly_payment + 10

print 'Monthly payment to pay off debt in 1 year: ' + str( mini_monthly_payment)
print 'Number of months needed: ' + str(total_months)
print 'Balance: ' + str( remaining_balance)  
