import math as m 
import decimal as d
import time
medeltid=0
antal=int(input("Hur många primtal? "))
antalupprepningar = int(input("hur många upprepningar? "))
st=time.time()
for x in range (antalupprepningar+1):
    st1=time.time()
    tal=1
    primLista=[2] # Anta första primtalet
    tider=[]
    while True:
        tal+=2 # Alla primtal är udda, så vi kan sortera bort alla tal delbara med 2
        antalTal=len(primLista)
        for i in range (antalTal):
            primtal=primLista[i] # Hämta ut ett specifikt primtal från listan
            if tal%primtal: # Om tal/primtal har en rest kan talet tillfälligt konstateras prim
                ärPrim=True
            else: # Om tal/primtal endast en gång är delbara med varandra konstateras talet ej prim
                ärPrim=False
                break # Avsluta for-loopen
        if ärPrim==True: 
            primLista.append(tal) # Om talet bestämts till prim så läggs det till i listan av primtal
        if len(primLista)>=antal: # Upprepa till ett visst antal primtal räknats ut
            break
    d.getcontext().prec=m.ceil(antal**0.5) # Bestäm antal decimaler för ökad säkerhet 
    pi=d.Decimal(1)
    for i in range (len(primLista)):
        pi*=d.Decimal(1)/(d.Decimal(1)-d.Decimal(primLista[i]**(-2))) # Uppskatta pi som en produkt av alla primtalen
    et1=time.time()
    print("Loop ", x, " time elapsed: ", et1-st1)
et=time.time()
print(primLista)
print((6*pi)**d.Decimal(0.5)) # Skriv ut pi
print(antal, "primes, time elapsed: ", (et-st)/(antalupprepningar+1))
