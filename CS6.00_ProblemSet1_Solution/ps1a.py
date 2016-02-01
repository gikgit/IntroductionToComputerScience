outstanding_balance = float(raw_input('the outstanding balance on the credit cart: '))
annual_interest = float(raw_input('annual interest rate: '))
mini_monthly_payment_rate = float(raw_input('minimum monthly payment rate: '))

month_total = 12
count = 1
mini_monthly_payment = 0
interest_paid = 0
principal_paid = 0
remaining_balance = 0
sum = 0

while count <= month_total:
    mini_monthly_payment = mini_monthly_payment_rate * outstanding_balance
    interest_paid = (annual_interest / 12) * outstanding_balance
    principal_paid = mini_monthly_payment - interest_paid
    remaining_balance = outstanding_balance - principal_paid
    print 'Month:' + ' ' + str(count)
    print 'Minimum monthly payment:' + ' ' + '$' + str(mini_monthly_payment)
    print 'Principal paid:' + ' ' + '$' + str(principal_paid)
    print 'Remaining balance:' + ' ' + '$' + str(remaining_balance) 
    count = count + 1
    sum = sum + mini_monthly_payment
    outstanding_balance = remaining_balance

print 'RESULT'
print 'Total amount paid:' + ' ' + '$' + str(sum)
print 'Remaining balance:' + ' ' + '$' + str(outstanding_balance)
