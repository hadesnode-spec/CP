
def find_one(n):
    for i in range(5):
        for j in range(5):
            if(n[i][j]==1):
                return (i,j)

n,m=5,5
a=[]
for _ in range(5):
    a.append(list(map(int,input().split())))
pos_one=find_one(a)
ans=abs(pos_one[0]-2)+abs(pos_one[1]-2)
print(ans)    
