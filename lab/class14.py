# def fibo(alpha):
#     n=alpha+1
#     nfib = [0,1]
#     for i in range(3,n+1):
#         nfib.append(nfib[i-2]+nfib[i-3])
#     return nfib[n-1]

# print(fibo(40))

# def fibo(a):
#     global x
#     x+=1
#     if a==0:
#         return 0
#     if a==1:
#         return 1
#     dic = {0:0, 1:1}
#     # # if a in dic:
#     if(a in dic):
#         return dic.get(a)
#     dic[a] = fibo(a)

#     return fibo(a-1) + fibo(a-2)

# x=0
# print(fibo(3))
# print(x)
# dic = {0:0, 1:1}
# print(dic.get(1))