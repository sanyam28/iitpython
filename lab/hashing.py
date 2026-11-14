a="where are you?"
b="where are you."

def compare(a,b):
    if len(a)!=len(b):
        return False
    try:
        i=0
        while True:
            if a[i] == b[i]:
                i+=1
                continue
            else:
                return False
    except:
        return True

print(compare(a,b))
hashcode = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    " ": 27,
    ".": 28,
    "?": 29
}

def hashvalue(x):
    b=0
    for i in x:
        b+=hashcode.get(i)
    return b

print(hashvalue(a))

z='abcdefghijklmnopqrstuvwxyz .?'
dic = {}

def create(z):
    global dic
    for i in range(len(z)):
        dic[z[i]] = i+1

create(z)
print(dic)

