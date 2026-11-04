def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterm = int(input("Enter the number of terms(greater than 0): "))

if nterm <= 0:
    print("Please enter the positive integer.")
else:
    print("Fibonacci sequence")
    for i in range(nterm):
        print(recur_fibo(i))
