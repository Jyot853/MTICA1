num=int(input("enter your number:"))
sum=0
temp=num
while(num>0):
    r=num%10
    sum=sum+r*r*r
    num=num//10
if temp==sum:
    print("armstrong")
else:
    print("not armstrong")





'''output:
===================  

enter your number:370
armstrong

=================== 
enter your number:371
armstrong

=================== 
enter your number:123
not armstrong

=================== 
enter your number:1634
not armstrong'''
