def fibo(n):
    nfib = [0,1]
    for i in range(3,n+1):
        nfib.append(nfib[i-2]+nfib[i-3])
    print(nfib[n-1])

a= int(input('nth fibo: \n'))
fibo(a)