# A basic code for matrix input from user 
n=int(input())
f=[]
g=[]
for j in range(n):
    ref=int(input())
    g.append(ref)
    for i in range(ref):
        f.append(int(input()))
print(g)
print(f)    
count=1
for i in range(len(g)):
    n=g[i]
    ku =f[0:n]
    print(ku)
    for p in range(n):
        f.pop(0)
        print("pop ke baad",f)
    for lo in range(len(ku)-1):
        if(ku[lo]<ku[lo+1]):
            print("ku mein aaye")
            ku[lo+1]=ku[lo]
        else:
            count+=1
    print("count kiya")
    print(count)
    count=1