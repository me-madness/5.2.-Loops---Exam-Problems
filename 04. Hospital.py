period = int(input()) 
doctors = 7
treated_patient = 0
untreated_patient = 0

for day in range(1, period+1):
    patients = int(input())
    if(day % 3 == 0) and (untreated_patient > treated_patient):
        doctors += 1
    if patients > doctors:
        treated_patient += doctors
        untreated_patient += patients - doctors   
    else:
        treated_patient += patients
        
print(f'Treated patients:{treated_patient}')        
print(f'Untreated patients:{untreated_patient}')        