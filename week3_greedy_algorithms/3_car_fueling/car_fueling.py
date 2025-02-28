from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    refils=0
    currentposition=0
    stops.append(distance)
    stops.insert(0, 0)

    i=0

    while currentposition <distance:
        lastposition=currentposition
        while i< len(stops) and stops[i] <=currentposition+tank:
             lastposition=stops[i]
             i+=1
        if lastposition ==currentposition:
            return -1
        if lastposition < distance:
            refils+=1
        currentposition=lastposition
    return refils







if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
