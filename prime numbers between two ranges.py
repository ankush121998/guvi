#author="ankush"
def isprime(n):
    if(n==2 or n==3):
        return True
    elif(n<=1):
        return False
    elif(n%2==0 or n%3==0):
        return False
    else:
        x=5
        while(x*x<=n):
            if(n%x==0 or n%(x+2)==0):
                return False
            x+=6
        return True
m,n=map(int,input().split())
for i in range(m+1,n):
    if(isprime(i)):
        print(i,end=" ")
