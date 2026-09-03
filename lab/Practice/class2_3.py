x = int(input("Enter you no.: "))

smallest_divisor = None

for divs in range(2,x):
    if x%divs == 0:
        smallest_divisor = divs
        break

if smallest_divisor != None:
    print(f'The largest divisior of {x} is {int(x/smallest_divisor)}')

else:
    print(f'{x} is a prime number.')