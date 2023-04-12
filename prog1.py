##wap to find the number of each character present in string

s=input("enter a value of string")
l=[]

for i in s:
    if i not in l:
        l.append(i)
        print(l)
for i in sorted(l):
    print("{} repated {}".format(i,s.count(i)))