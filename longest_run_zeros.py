import random
data=[]
for ii in range(100):
    temp=random.randint(0,1)
    data.append(temp)
print(data)
count=0
for ii in data:
    if(ii==0):
        count=count+1
print("No.of zeros=",count)