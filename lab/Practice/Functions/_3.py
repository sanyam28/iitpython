def mult(b):
    if len(b) == 0 :
        return "List can't be empty"
    elif len(b) ==1:
        return b[0]
    else:
        a=1
        for i in b:
            a*=i
        return a


a = input('Enter numbers with spaces: \n')
b = [int(x) for x in a.split(' ')]
print(mult(b))