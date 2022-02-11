import math
def factors(num):
    count=2
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
           count+=1 if num//i==i else 2
        return count if num> 2 else num
        
n=int(input("enter a number::"))
print("N0.of factors for ",n,":",factors(n))
