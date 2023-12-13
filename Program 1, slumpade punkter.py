import random as r
import math as m
import decimal as d
def piApprox(n):
    inne=0
    for i in range (n):
        d.getcontext().prec=n # Bestäm antal decimalplatser för ökad säkerhet
        x=r.random() # Slumpa ut x- och y-värde
        y=r.random()
        if (m.sqrt(d.Decimal(x)**2+d.Decimal(y)**2)<=1): # Pythagoras sats för att bestämma avstån till origo
            inne+=1 # Räkna hur många som faller inom cirkelns area
    pi=4*inne/n # Uppskatta pi
    return pi
print(piApprox(int(input("Välj ett tal: "))))