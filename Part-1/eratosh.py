
Max = 99999

isprime = [True for d in range(Max)]

isprime[0] = isprime[1] = False

for i in range(2,int(Max**(1/2))+1):
    if isprime[i]:
        for j in range(i**2,Max,i):
            isprime[j] = False

primes = [i for i in range(Max) if isprime[i]]

n = int(input())

if n==0:
    print("plz enter number greater than zero")
else:
    print(sum(primes[:n]))
       
