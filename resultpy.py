sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
  if(avg>=90):
    print("first class")
  elif(avg>=80&avg<=90):
    print("second class")
  elif(avg>=70&avg<=80):
    print("avg")
  elif(avg>=60&avg=<70):
    print("pass")
  else:
    print("fail")
    