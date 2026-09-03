def enjoy():
    for i in range(0,11):
        print(i)

enjoy()

def addNumber(iu1, iu2):
    sum = iu1 + iu2
    print(sum)
    return sum

addNumber(4,6)

print("Let's sum two numbers:")
fir1 = int(input("Choose your first number: "))
fir2 = int(input("Choose your second number: "))

addNumber(fir1, fir2)

print("Lets Calculate Length of string")

def lenstr(string):
    lenval = len(string)
    print(lenval)

print("Caution: spaces will be considered")
inpstr = input("Enter your string for which you want length of that string: ")
lenstr(inpstr)

print("Buddy, its time to upgrade")
def main():
    a = 0.0
    b=range(10)

    for i in b:
        print(i)

        a+=0.1
        print(a)

    print(a)

main()

