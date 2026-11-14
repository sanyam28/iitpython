import math

# Write a python function prime(x) which returns True if x is prime and False otherwise.
# A function to check whether given number is prime or not
def isPrime(y):
    if y==1:
        return False
    if y==2:
        return True
    if y%2==0:
        return False
    for i in range(3, int(math.sqrt(y))+1, 2):
        if y%i==0:
            return False
    return True

# Example
print("Is 47 is a Prime number",isPrime(47)) #Print True, as 47 is a prime number

# Write a python function prime_list(n) which returns a sorted list of prime numbers between 2 and n
# for numbers>=2, sorted prime list function  to get between 2 and n
def prime_list(n):
    out =[]
    out.append(2)
    for i in range(3,n+1,2):
        if isPrime(i):
            out.append(i)
    return out

print("prime_list between 2 and 34", prime_list(34))

# Write a python function erastolist(n) which returns a list of all numbers between 2 and n which are not multiples of 2 and 3. 
# Erasto List function to return numbers between 2 and n which are not multiple of 2 and 3, where n is given natural number >=2
def erastolist(n):
    ilist = [2,3,5]
    state = True
    while True:
        if ilist[len(ilist)-1]>n:
            break
        if state:
            ilist.append(ilist[len(ilist)-1]+2)
            state=False
        else:
            ilist.append(ilist[len(ilist)-1]+4)
            state=True
    ilist.pop()
    return ilist

print("erasto list for n=44",erastolist(44))

# Write a python function erasto_prime_list(n) which returns all prime numbers between 2 and n using the Sieve of Erastothenes method. 
# Erasto Prime List function to return all prime number between 2 and n using Sieve of Erastothenes method
def erasto_prime_list(n):
    prime_list = []
    temp = []
    for i in range(2,n):
        temp.append(i)

    for i in range(2, int(math.sqrt(n))+1):
        for x in range(i,n,i):
            if x!=i and temp[x-2]>0:
                temp[x-2] = -temp[x-2]
    for prime in temp:
        if prime>0:
            prime_list.append(prime)
    return prime_list

print("Erasto Prime List for n=44",erasto_prime_list(44))