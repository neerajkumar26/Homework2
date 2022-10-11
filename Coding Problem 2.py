# Name: - Neeraj Kumar
# ID: - 2047559
from datetime import datetime





###########################
correctDates = []
filename = 'inputDates.txt'
with open(filename,"r") as fin:
    last_date = fin.read().split('\n')
    # print(last_date)
    
    for date in last_date:
        try:
            my_date = datetime.strptime(date, '%B %d, %Y')
            correctDates.append(my_date)
        except Exception as e:
            pass
# print(correctDates)
i=0
f = open("parsedDates.txt", "w")
for _date in correctDates:
    print(f'writing {i+1}')
    print(f'{_date.month}/{_date.day}/{_date.year}')
    f.write(f'{_date.month}/{_date.day}/{_date.year}\n')
    i=i+1
f.close()