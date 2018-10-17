char=input()
if(char>='a' and char<='z'):
    if(char in ['a','e','i','o','u']):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
