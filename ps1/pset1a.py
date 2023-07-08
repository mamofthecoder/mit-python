
annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion saved: "))
total_cost = float(input("Enter total cost: "))

portion_down_payment= 0.25
# r is the annual rate
r = 0.04
#monthly rate
monthly_rate = r/12
# down payment of house
down_payment = total_cost*portion_down_payment
#monthly salary
monthly_salary = annual_salary/12
#number of months starting at 0
months = 0
#The amount of money saved monthly
monthly_saved = monthly_salary*portion_saved
#csavings at the beginning
current_savings = 0
#while the current savings are less than the down payment
while current_savings<=down_payment:
    #add the monthly rate and the amount saved monthly to our current savings
    current_savings += current_savings*monthly_rate
    current_savings += monthly_saved
    months = months+1
print("Number of months: ",months)
