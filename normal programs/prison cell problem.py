n= int(input("enter no of prison cells: "))
p=int(input("enter no of prisoners:"))
i=1
d={}
#initialising the dictionary
for m in range(1,n+1):
    d[m]=0
while(i<=n):
    for j in range(i,n+1):
        d[j]+=1
        if(p<=0):
            print("p",p)
            print("in")
            i=n
            break
        p-=1
    i+=1    
if(p>=0):
   d[1]+=p
print(d)        
