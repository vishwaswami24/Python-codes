str1=input('Enter the strings:')

v=0
c=0
for str in str1:
    if str in ('a','e','i','o','u','A','E','I','O','U'):
       v+=1
    else:
        c+=1
print('Count of vowel:',v)
print('Count of consonant:',c)

