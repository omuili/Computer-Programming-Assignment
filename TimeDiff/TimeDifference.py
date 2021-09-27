time_1=input('Enter Earlier Time: ')

time_2=input('Enter Later Time: ')

h1,m1=time_1.split(':')
h2,m2=time_2.split(':')

earlierMinutes=0
laterMinutes=0

if m1[-2:].lower()=='am':
    earlierMinutes+=int(h1)*60+int(m1[:2])
else:
    if int(h1)!=12:
        earlierMinutes+=int(h1)*60+int(m1[:2])+12*60
    else:
        earlierMinutes=12*60+int(m1[:2])

if m2[-2:].lower()=='am':
    laterMinutes+=int(h2)*60+int(m2[:2])
else:
    if int(h2)!=12:
        laterMinutes+=int(h2)*60+int(m2[:2])+12*60
    else:
        laterMinutes=12*60+int(m2[:2])

difference=laterMinutes-earlierMinutes
if difference<0:
    difference=1440+difference
hrs=difference//60
mins=difference%60

print()
print('Number of minutes between',time_1,'and',time_2,'=',difference)
print('The time difference between',time_1,'and',time_2,'=',hrs,'hours and',mins,'minutes.')