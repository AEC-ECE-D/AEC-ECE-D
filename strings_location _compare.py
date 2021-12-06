def first_diff(str1,str2):
    flag=-1
    length1=len(str1)
    length2=len(str2)
    length=0
    if(length1<=length2):
        length=length1
    else:
        length=length2
    for ii in range(length):
        if (str1[ii]!=str2[ii]):
            flag=ii+1
            break
    return flag
str1=input(" enter the 1st string:::")
str2=input(" enter the 2st string:::")
location=first_diff(str1,str2)
print(location)
