def change(money):
    # write your code here
    coins =[10,5,1]
    count=0
    for coin in coins:
            count+=money//coin
            money=money%coin
            if money ==0:
                 break
    return count



if __name__ == '__main__':
    m = int(input())
    print(change(m))
