import math
#1.feladat (nem igazán az, de mindegy)
"""
for i in range(0,50):
    print(i)

for i in range (57,89):
    if (i%2)!=0:
        print(i)

for i in range (1,20):
    print (i and math.sqrt(i))
   
for i in range (1000,0):
    print(i)
     

#2.feladat:

for i in range (50):
    print(i*"*")

num = int(input("Hányszor"))
what=  str(input("Mit?"))

for i in range (num):
    print(what)


text= str(input("Kérek egy szöveget!"))
num=(len(text))
for i in range (num):
    print("*"*i, end="")
print("\n*",text,"*")
for i in range (num):
    print("*"*i, end="")

for i in range (4*"*"):
    print(i, end="")
    """

for i in range (8):
    print(i, end="")
    print("* "*5)
    for i in range (4):
        print("*")





#3.feladat:



#44.feladat:
"""
num= int(input("Kérek egy évszámot!"))

if   (num%400)==0 and (num%100)!=0:
    print("Szökőév!")
elif (num%4)==0 :
    print("szökőév!")
else:
    print("Nem szökőév!")

#44.feladat:
num= int(input("Kérek egy évszámot!"))

if (num%4)==0 or ((num%400)==0 and (num%100)!=0):
    print("szökőév")
else:
    print("Nem szökőév!")
#3.próba egy sorba?


#Ciklusok:
for i in range(3):
    x =int(input("Kérek egy számot"))
    print("az/a {i}szám  a(z) {x}")

for i in range(3):
    x =int(input("Kérek egy számot"))
    if(x%2==0):
        print("páros")
    else :
        print("nem páros")

for i in range(3,108,12):
    print(i)
"""