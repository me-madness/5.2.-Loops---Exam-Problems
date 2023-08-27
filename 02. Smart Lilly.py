age = int(input())
washing_machine_price = float(input())
toy0price = int(input())

toy_count = 0
sum = 0
money = 10


for year in range(1, age+1):
    if year%2==0:
        
        sum += money
        money = money + 10
    else:
        toy_count += 1
