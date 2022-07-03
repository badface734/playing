import montyHall
ygoat = 0
ycar = 0
ngoat = 0
ncar = 0

for x in range(1000):
    mh = montyHall.montyHall('y')
    if  mh == 'goat':
        ygoat += 1
    elif mh == 'car':
        ycar += 1

for x in range(1000):
    mh = montyHall.montyHall('n')
    if  mh == 'goat':
        ngoat += 1
    elif mh == 'car':
        ncar += 1

print('results for changing your guess:')
print('goat: '+str(ygoat))
print('car: '+str(ycar))
print(ycar / 10)

print('results for not changing your guess:')
print('goat: '+str(ngoat))
print('car: '+str(ncar))
print(ncar / 10)

