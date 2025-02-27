def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a, b):
    return (a//gcd(a,b))*b



if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

