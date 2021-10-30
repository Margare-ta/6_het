N=int(input("Kérek egy számot!"))

for j in range(1,N):
    num=0
    for i in range(1,j+1):
        if j%i==0:
            num=num+1
    if num==2:
        print(j)
    
