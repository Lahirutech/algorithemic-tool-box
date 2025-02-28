from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.


    # write your code here
    while capacity>0 and len(values)>0:
        maxval=0
        maxValindex=-1
        for i in range(len(values)):
            valperUnit=values[i]/weights[i]
            if valperUnit > maxval:
                maxval =valperUnit
                maxValindex=i

        if weights[maxValindex]>=capacity:
            value+=maxval*capacity
            capacity=0
        else:
            value+=maxval*weights[maxValindex]
            capacity -= weights[maxValindex]
            weights.pop(maxValindex)
            values.pop(maxValindex)
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
