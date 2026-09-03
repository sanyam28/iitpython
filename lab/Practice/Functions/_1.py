def str_chk(a,b):
    if a in b or b in a:
        return True
    return False
print("Let's check if any one of string is contained in another")
a= input('Enter First string: ')
b= input('Enter Second string: ')
print(str_chk(a,b))