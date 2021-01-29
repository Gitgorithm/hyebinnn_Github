finish=input()
eng='a'
while ord(eng)<=ord(finish):
    print(eng, sep=" ")
    eng = chr(ord(eng)+1)
    
