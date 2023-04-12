##Python code to convert lowercase character to uppercase character of string
s=input("enter a string")
a=""
for i in s:
        if i.islower():
            i = i.upper()
        a=a+i
print("String after converting lower case to upper :",a)