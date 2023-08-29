n = int(input())
p1 = 0
p2 = 0
p3 = 0

p1_count = 0
p2_count = 0
p3_count = 0
for num in range(n):
    current_num = int(input())
    
    if current_num % 2 == 0:
        p1_count += 1
    if current_num % 3 == 0:
        p2_count += 1
    if current_num % 4 == 0:
        p3_count += 1    

p1 = p1_count / n * 100
p2 = p2_count / n * 100
p3 = p3_count / n * 100

print("%.2f" % p1 + "%")
print("%.2f" % p2 + "%")
print("%.2f" % p3 + "%")      