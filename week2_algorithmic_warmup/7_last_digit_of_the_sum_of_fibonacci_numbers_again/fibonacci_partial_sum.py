# Uses python3
import sys

def calculate_fib(n):
    if n<=1:
        return n

    a,b=0,1
    for _ in range (n-1):
        a,b=b,a+b
    return b%10


def fibonacci_partial_sum_naive(from_, to):
    from_ =from_%60
    to =to%60
    if to < from_:  # Handle wrap-around case
        to += 60
    fibFrom=calculate_fib(from_+1)
    toFib=calculate_fib(to+2)
    return (toFib-fibFrom)%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
