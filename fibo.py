def fibo(n):
    if fibo(n<=1):
        return 1
    else:

        return (fibo(n-1)+fibo(n-2))
    for i in range (n):
        print(fibo(i))