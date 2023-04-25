num=int(input("enter the number:"))
sum_v=0
for i in range(1,num):
    if(num%i==0):
        sum_v=sum_v+i
    if(sum_v==num):
        print("the enter number is prefect number")
    else:
        print("the enter number is not a prefect number")