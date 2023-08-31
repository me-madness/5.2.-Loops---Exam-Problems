count_packages = int(input())
bus = 0
truck = 0
train = 0
sum_packages = 0
sum_midlle_price = 0
bus_count = 0
truck_count = 0
train_count = 0

for i in range(count_packages):
    tons = int(input())

    if tons <= 3:
        bus_count += tons
    elif 3 < tons <= 11:
        truck_count += tons
    else:
        train_count += tons  
 
sum_packages = bus_count + truck_count + train_count
sum_midlle_price = (bus_count * 200 + truck_count * 175 + train_count * 120) / sum_packages
bus = bus_count / sum_packages * 100
truck = truck_count / sum_packages * 100
train = train_count / sum_packages * 100


print(round(sum_midlle_price, 2))
print(f'{bus} %')
print(f'{truck} %')
print(f'{train} %')