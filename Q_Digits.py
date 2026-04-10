t=int(input())
 
for i in range(t):
    i=int(input().strip())
 
    if i==0:
        print(0)
    else:
 
 
        while i>0:
           
 
           print(i%10,end=" ")
           i=i//10
        print()    