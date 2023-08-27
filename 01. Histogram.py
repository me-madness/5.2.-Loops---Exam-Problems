n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(n):
    current_num = int(input())
    if current_num < 200:
        p1_count += 1
    elif current_num >= 200 and current_num < 399:
        p2_count += 1
    elif current_num >= 400 and current_num < 599:
        p3_count += 1
    elif current_num >= 600 and current_num < 799:
        p4_count += 1
    else:
        p5_count +=1
p1 = (p1_count / n) * 100        
p1 = (p2_count / n) * 100        
p1 = (p3_count / n) * 100        
p1 = (p4_count / n) * 100        
p1 = (p5_count / n) * 100        
            
print(f"{round(p1)} % ")
print(f"{round(p2)} % ")
print(f"{round(p3)} % ")
print(f"{round(p4)} % ")
print(f"{round(p5)} % ")
