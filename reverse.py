word1=input("enter string 1:")
word2=input("enter string 2:")
if len(word1)==len(word2):
    word="    "
    for i in range(len(word1)):
       word+=word2[i]+word1[i]
    print(word)
else:
    print(" given strings are not equal")
    
