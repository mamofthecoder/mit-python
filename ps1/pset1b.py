annual_salary = float(input("Enter annual salary: "))
portion_saved = float(input("Enter portion saved: "))
total_cost = float(input("Enter total cost: "))
semi_annual_raise = float(input("Enter semi annual raise: "))

portion_down_payment= 0.25
# r is the annual rate
r = 0.04
#monthly rate
monthly_rate = r/12
# down payment of house
down_payment = total_cost*portion_down_payment
#monthly salary
months = 0
#csavings at the beginning
current_savings = 0
#while the current savings are less than the down payment
while current_savings<=down_payment:
    #monthly salary
    monthly_salary = annual_salary/12
    #The amount of money saved monthly
    monthly_saved = monthly_salary*portion_saved
    #add the monthly rate and the amount saved monthly to our current savings
    current_savings += current_savings*monthly_rate
    current_savings += monthly_saved
    months = months+1
    #check if 6 months have passed to add salary increase
    if months%6==0:
        annual_salary += annual_salary*semi_annual_raise 
print("Number of months: ",months)
