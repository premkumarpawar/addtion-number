def check(s2,s1):
    if (s2.count(s1)>0):
        print("second string is substring of the first string")
    else:
        print("second string is not  substring of the first string")
s2="the sqauer root of a given number"
s1="root"
check(s2,s1)