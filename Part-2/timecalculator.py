from datetime import datetime
print("enter number of hours you want to work :")
totalhrs = int(input())
print("enter time you entered (HH:MM):")
entrytime = input()

l2 = entrytime.split(':')
entryhr = int(l2[0])
entrymin = int(l2[1])

now = datetime.now()
current_time = now.strftime("%H:%M")
l3 = current_time.split(':')
currhr = int(l3[0])
currmin  = int(l3[1])

remaining_hr = (totalhrs - (currhr-entryhr))
remaining_min = abs(entrymin - currmin)
if remaining_hr == 0:
    print("you have completed your desired work hours")
else:
    print("you have ",remaining_hr," hour and ",remaining_min," minutes left")



