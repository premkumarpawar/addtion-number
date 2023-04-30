s1=input("enter the first string")
s2=input("enter the second string")
a=list(set(s1)&set(s2))
print("the comman letters are:")
for i in a:
    print(i)