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
    

for i in range (8):
    print(("* "*3)*7)
    for i in range (2):
        print(("*    ")*9)
# utolsó sorban hogyan legyen teljes sor?


#3.feladat:
#változó külön névvel for ciklusban?
num= int(input("Kérek egy egész számot!"))
num2= int(input("Kérek egy egész számot!"))

if num<num2 or num==num2:
    for i in range(num,num2+1):
        print(i)
elif num>num2:
    for i in range(num2,num+1):
        print(i)


#4.feladat

for i in range(1,44):
    print(round(math.pow(i,2)),"; ", end="", sep="")

#5.feladat:

num= int(input("Hanyadik egész számig írja ki a szám köbét a program?"))

for i in range (1,num+1):
    print(round(math.pow(i,3)))

#6.feladat:

a= int(input("Kérek egy számot!"))
b= int(input("Kérek egy számot!"))

for i in range(a,b):
    print(round(math.sqrt(i),2))
#Ez így jó?
"""
#7.feladat:

n= int(input("Kérek egy számot!"))

for i in range(2,n):
    num=(i*i-i)
print("n!=",num)

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