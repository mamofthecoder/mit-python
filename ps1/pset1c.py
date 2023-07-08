import math

starting_salary = float(input("Enter annual salary: "))
total_cost = 10**6
portion_down_payment= 0.25
semi_annual_raise = 0.07
# r is the annual rate
r = 0.04
#monthly rate
monthly_rate = r/12
# down payment of house
down_payment = total_cost*portion_down_payment
#bisection lower bound and upper bound
lower_bound = 0
upper_bound = 1
steps = 0
#the acceptable difference
acceptable_diff = 100
#initialize target difference
target_diff = down_payment*2
#while the current savings are less than the down payment
while abs(target_diff)>acceptable_diff and steps<100:
    portion_saved = (lower_bound+upper_bound)/2
    #savings at the beginning
    current_savings = 0
    #months at the beginning
    months = 0
    #reset annual salary for bisection
    annual_salary = starting_salary
    while months < 36:
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
    #check how far from target savings
    target_diff = down_payment - current_savings
    # saved below down payment
    if target_diff > 0:
        lower_bound = portion_saved
    # saved over down payment
    elif target_diff<0:
        upper_bound = portion_saved
    steps +=1
else:
    #checks if target is reached
    if abs(target_diff) <= acceptable_diff:
        #print the saving rate to 4 decimal places and the number of bisection steps
        print(f"Best saving rate: {round(portion_saved,4)}")
        print(f"Steps in bisection search: {steps}")
    else:
        print("cannot find portion_saved")
