import math
import decimal
import time
digit =int(input("what decimal? "))
st=time.time()
def sum(n):
    pi=decimal.Decimal(0)
    for i in range (n+1):
        decimal.getcontext().prec=math.ceil(n**(1+1/n))
        pi+=decimal.Decimal(1)/(16**i)*(decimal.Decimal(4)/(8*i+1)-decimal.Decimal(2)/(8*i+4)-decimal.Decimal(1)/(8*i+5)-decimal.Decimal(1)/(8*i+6))
    pi=str(pi)
    nypi=decimal.Decimal(3)
    piList=[*pi]
    piList.pop(0)
    piList.pop(0)
    delta=math.ceil(n**(1+1/n))-1-n
    for i in range (delta):
        piList.pop(len(piList)-1)
    for i in range (len(piList)):
        piList[i]=decimal.Decimal(piList[i])
        nypi+=piList[i]/(10**(1+i))
    global y
    global result
    result =str(nypi)
    y = len(str(nypi))-2
    #return str(nypi)
sum(digit)
with open('piapproxBBP.txt', 'w') as f:
    f.write(result)
    f.close()
print(result)
print(y)
et=time.time()
print("time elapsed: ", et-st)