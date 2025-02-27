def get_pisano_period(m):
    prev, curr = 0, 1
    for i in range(0, m * m):  # Pisano period is at most m*m
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1

def fibonacci_huge_naive(n, m):
    n=n%get_pisano_period(m)
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current if n else 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
