def fibo (n):
    if n in (1,2):
        return 1
    elif n>2:
        return fibo(n-1)+fibo(n-2)


print(fibo(5))
print(fibo(7))


#1 1 2 3 5 8 13
