
def f1(n):
    global count1
    count1+=1
    if n<0:
        return "n can't be negative"
    if n ==0:
        return 0
    if n == 1:
        return 1
    return f1(n-1) + f1(n-2)
dic = {0:0, 1:1}
def f2(n):
    global count2
    count2+=1
    if n<0:
        return "n can't be negative"
    if n ==0:
        return 0
    if n == 1:
        return 1
    if dic.get(n) != None:
        return dic[n]
    if dic.get(n-1)!= None and dic.get(n-2)!= None:
        dic[n] =dic[n-1]+dic[n-2]
        return dic[n-1]+dic[n-2]
    return f2(n-1) + f2(n-2)

count1=0
count2=0
print('As disccused in class, value of 20th fibonacci no using recusrssion without dictionary', f1(20))
print('Count for this', count1)
print('using dictionary, value of 30th fibonacci no',f2(30))
print('count using dictionary', count2)