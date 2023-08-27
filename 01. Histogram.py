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
    elif current_num >= 200 and current_num <= 399:
        p2_count += 1
    elif current_num >= 400 and current_num <=599:
        p3_count += 1
    elif current_num >= 600 and current_num <= 799:
        p4_count += 1
    else:
        p5_count +=1
p1 = p1_count * 100 / n       
p2 = p2_count * 100 / n        
p3 = p3_count * 100 / n        
p4 = p4_count * 100 / n        
p5 = p5_count * 100 / n       
            
print("%.2f" % p1 + "%")
print("%.2f" % p2 + "%")
print("%.2f" % p3 + "%")
print("%.2f" % p4 + "%")
print("%.2f" % p5 + "%")
