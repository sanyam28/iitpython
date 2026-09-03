y=float(input('etnter'))
i = 0 
noi =0
while True:
    i = i + 0.0001
    noi+=1
    if abs(i*i-y) < 0.01:
        break 


print(i)
print(noi)
        