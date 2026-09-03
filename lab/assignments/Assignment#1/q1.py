print("Arithmetic Numbers")

a = int(input("Choose your first term of your A.P: "))
d= int(input("Choose common difference: "))

ap_dif_average = 0

print("10 arithementic progression numbers are: ")

for i in range(1,11):
    print(a + (i-1)*d)

    if i<10:
        ap_dif_average += d

print("Average of difference of consecutive terms of an A.P is: ")
print(abs(ap_dif_average/9))

print('Geometric Numbers')

c = int(input("Choose your first term of your G.P: "))
r = int(input("Choose common ratio: "))

gp_dif_avg = 0

print("10 Geometric Progression Numbers are: ")

for i in range(1,11):
    print(c*(r**(i-1)))

    if i<10:
        gp_dif_avg += c*(r**(i)) - c*(r**(i-1))

print('Average of difference of consecutive terms of this 10 terms Geometric Progression is: ')
print(abs(gp_dif_avg/9))

print("Harmonic Numbers")

har_first = int(input('Choose your first respricol harmonic Number: '))
har_dif = int(input("resiprocal common difference: "))

har_diff_avg = 0
print("10 Harmonic Progression Numbers are: ")

for i in range(1,11):
    print(1/(har_first+(i-1)*har_dif))

    if i<10:
        har_diff_avg = (1/(har_first+(i-1)*har_dif)) - 1/(har_first+(i)*har_dif)

print("Average of difference of consecutive terms of Harmonic progression numbers is: ")
print(abs(har_diff_avg/9))


