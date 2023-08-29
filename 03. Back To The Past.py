money_past = float(input())
year_in_past = int(input())
years = 18

for current_year in range(1800, year_in_past+1):
    if current_year % 2 == 0:
        money_past -= 12000
    else:
        money_past -= (12000 + 50 * years)
    years += 1    
        
if money_past > 0:
    print(f"Yes! He will live a carefree life and will have {money_past} dollars left.")
else:            
    print(f"He will need {abs(money_past)} dollars to survive.")