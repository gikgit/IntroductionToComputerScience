outstanding_balance = float(raw_input('the outstanding balance on the credit cart: '))
annual_interest = float(raw_input('annual interest rate: '))

mini_monthly_payment = 0
total_months = 0
remaining_balance = 0
previous_balance = 0
monthly_interesr_rate = annual_interest / 12.0

monthly_payment_lower_bound = outstanding_balance / 12.0
monthly_payment_upper_bound = (outstanding_balance * (1 + (annual_interest / 12.0)) ** 12.0) / 12.0 

while True:
    count = 1
    balance = outstanding_balance
    mini_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2.0
    while count <= 12:
        balance = balance * (1 + monthly_interesr_rate) - mini_monthly_payment
        count = count + 1
        if balance <= 0:
            break    
    if balance == 0 or previous_balance == balance:
        total_months = count - 1
        remaining_balance = balance
        break
    elif balance > 0:
        monthly_payment_lower_bound = mini_monthly_payment
        previous_balance = balance
    else:
        monthly_payment_upper_bound = mini_monthly_payment
        previous_balance = balance
        
print 'Monthly payment to pay off debt in 1 year: ' + str( mini_monthly_payment)
print 'Number of months needed: ' + str(total_months)
print 'Balance: ' + str( remaining_balance)  
