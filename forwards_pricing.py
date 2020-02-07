import math

if input("Do you want to calculate a Fair Fowrard Price (Y/N): ") == "Y":
    days_mat = int(input("Enter the days until maturity (put a 0 and hit enter if in months): "))

    if days_mat == 0:
        days_mat = float(input('Enter months to maturity: '))
        time = days_mat/12
    else:
        time = days_mat /365

    spot = float(input('Enter the spot price (dollars and cents only): '))
    risk_free = float(input("Enter the risk-free rate as a decimal: "))
    dividend = float(input("If there is a dividend enter it, if not enter 0: "))

    if dividend > 0:
        dividend_date = int(input("Enter the days until the dividend will be paid: "))
    else:
        dividend_date = days_mat+1

    if dividend_date < days_mat:
        fair_fwd_price = (spot - (dividend)*math.exp((dividend_date/365)*risk_free*-1))*(math.exp((time)*risk_free))
    else:
        fair_fwd_price = (spot)*(math.exp(time*risk_free))

    print(f'\nFair Forward Price = ${fair_fwd_price}')

    
'''
if input(" Do you want to calculate a Present Value? Y/N: ") == "Y":
    k = float(input("Enter the agreed upon strike/price of the contract: "))
    PV = 
'''