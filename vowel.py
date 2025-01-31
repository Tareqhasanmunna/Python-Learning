a=input("enter string: ")
vowel= ('a','e','i','o','u','A','E','I','O','U')
for i in a:
    if i == ' ':
        continue
    if i in vowel:
        print(i,",vowel")
    else: print(i,",constant")