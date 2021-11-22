import random
def longest_zero_runlength(bin_list):
    max=0
    count=0
    for x in bin_list:
        if x==0:
            count+=1
        else:
            if count>max:
                max=count
            count=0
    return max
bin_list=[random.randint(0,1) for x in range(100)]
ret=longest_zero_runlength(bin_list)
print("Binary list:",bin_list)
print("longest run of zeros=", longest_zero_runlength(bin_list))