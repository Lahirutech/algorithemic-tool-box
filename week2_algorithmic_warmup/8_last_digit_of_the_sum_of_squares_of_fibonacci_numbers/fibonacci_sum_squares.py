
def calculate_fib(n):
    if n<=1:
        return n

    a,b=0,1
    for _ in range (n-1):
        a,b=b,a+b
    return b%10

def fibonacci_sum_squares(n):
    n=n%60
    fibn=calculate_fib(n)
    fibn2=calculate_fib(n+1)
    return (fibn*fibn2)%10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
