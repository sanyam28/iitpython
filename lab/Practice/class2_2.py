# Sum of Prime numbers greater than 2 but lesser than 999

sum = 0
for i in range(3,1000,2):
    condition = True
    for s in range(2,i):
        if i%s == 0:
            condition = False

    if condition:
        sum+=i

print(sum)