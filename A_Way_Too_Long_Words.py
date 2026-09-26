n=input()
for _ in range(int(n)):
    word=input()
    if(len(word)<=10):
        print(word)
    else:
        print(word[0]+""+str(len(word[1:len(word)-1]))+""+word[-1])
