count_packages = int(input())
bus = 0
truck = 0
train = 0
sum_packages = 0

bus_count = 0
truck_count = 0
train_count = 0
for i in range(count_packages):
    weight_packages = int(input())

    if weight_packages <= 3:
        bus_count += 1
    elif 3 < weight_packages <= 11:
        truck_count += 1
    else:
        train_count += 1  
 
bus = bus_count / count_packages * 100
truck = truck_count / count_packages * 100
train = train_count / count_packages * 100
sum_packages = bus_count + truck_count + train_count

               