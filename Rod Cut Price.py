def max(a,b):
    return a if a>b else b

def maxCutRoad(price, n):
    mx = 0
    if n<=0:
        return 0

    for i in range (0,n):
       # print (i)
        mx = max (mx, price[i] + maxCutRoad(price,n-i- 1))
       # print (mx)
    return mx

price=[4,7,6,9,3,6,7,6]
ln = len(price)
print (maxCutRoad(price, ln))


