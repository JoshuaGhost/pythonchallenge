data="map"

for i in data:
    if i.isalpha():
        print(chr((ord(i)-ord('a')+2)%26+ord('a')),end="")
    else:
        print(i,end="")

