import math

#-------------------------------------Calculation of Fair Foward Value-------------------------------------
print("\n" + "Fair Value Forward Price Calculation" + "\n" + "="*90)

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

#-------------------------------------Calculation of Present Value of Forward Contract-------------------------------------

print("\n" + "Present Value Calcuation" + "\n" + "="*90)

strike = float(input("Enter Strike Price: "))
contracts = float(input("Enter number of shares if short, negative: "))

if strike != 0:
    PV = contracts * (fair_fwd_price - strike) * (math.exp((time)*risk_free*-1))

print(f"\nPV = ${PV}")

