##Python code to convert uppercase  character to lower character of string
s=input("enter a string : ")
a=""
for i in s:
        if i.isupper():
            i = i.lower()
            print(i)
            a=a+i

print("String after converting lower case to upper :",a)