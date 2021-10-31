star=int(input("Mennyi csillagot írjak ki?(10 a legjobb(:))"))
star1=int(star*1.5)
print(star*"* ")
for i in range(star-2):
    print("*"," "*star1,"*")
print(star*"* ")
