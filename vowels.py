word =input("enter word:")
for ch in word:
    if ch in"a|e|i|o|u|A|E|I|O|U":
        print("word contain vowels")
        break
else:
    print("word doesnot contain vowels")
      
