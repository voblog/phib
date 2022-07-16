
print("fibanacci code thing")

def fib(n, memo={}):
    #1 1 2 3 5 8 13
    if (n <= 2):
        return 1 
    
    try:
        return memo[n]
    except:
        pass

    memo[n] = fib(n-2, memo)+ fib(n-1, memo)
    return memo[n] 

def f(n):
    s = fib(n)
    print(f"the {n} fibonacci number is {s}")

f(1)
f(2)
f(3)
f(4)
f(5)
f(6)
f(7)
f(8)
f(9)
f(10)
f(11)
f(12)
f(13)
f(14)
f(15)
f(20)
f(30)
f(40)
f(1000)