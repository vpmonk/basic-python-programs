n=int(input())  
og_n=n
res=0
while n!=0:
    rev = n%10
    res = res*10+rev
    n=n//10
if res==og_n:
    print("true")
else:
    print("false")        
