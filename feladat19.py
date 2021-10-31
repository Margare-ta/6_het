N=int(input("Kérek egy számot!"))

for i in range(0,N):
    print((" "*(N-i)),("*"*i),("*"*(i+1)),sep="")