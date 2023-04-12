###Python code to remove vowels from the string

st = input("Enter a String : ")

rlt=''
for i in st:

    if i in ('a', 'e', 'i', 'o', 'u') :
       i = ''
    rlt=rlt+i

print("String after removing the vowels :",rlt)