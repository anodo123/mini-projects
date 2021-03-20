a= int(input("enter the number of values"))
b=[]
for i in range(a):
    n= []
    n.append(int(input("enter the first value")))
    n.append(int(input("enter the second value")))
    b.append(n)
    print(n)
print(b)
c=[]
for i in range(a):
    for j in range(2):
        c.append(b[i][j])
print(c)
for i in range(len(c)):
    count =0
    for j in range(i+1,len(c)):
        if(c[i]==c[j]):
            print(len(c[i:j]))
        for o in range(i+1,len(c)):
            if(c[i]==c[o]):
               count =0
            else:
               count+=1
    if(count>0):
        print("2")