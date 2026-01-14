#Fibonacci Series
def fibonacci(n):
    count=1
    fn=0
    fn_minus_one=1
    fn_minus_two=1
    while count<=n:
        print(fn)
        fn_minus_two=fn_minus_one
        fn_minus_one=fn
        fn=fn_minus_one+fn_minus_two
        count+=1

N=int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci(N)