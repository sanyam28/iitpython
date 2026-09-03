print('Welcome!! , I will give you two numbers based on your provided number such that I will be like a^b = your no, and 1<b<6')

user_inp = int(input("Choose your no: "))

root =[] 
pwr = []

for i in range(2,6):
    ite = 1
    while ite**i < user_inp:
        ite+=1

    if ite**i == user_inp:
        root.append(ite)
        pwr.append(i)

if(len(root)==0):
    print('No such pair exist')

else:
    for i in range(len(root)):
        print(root[i], pwr[i])