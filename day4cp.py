import math
def checkprimenumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    count=int(math.sqrt(num))+1
    for i in range(2,count):
        if num%i==0:
            return 0
        return num
              

start=int(input())
stop=int(input())
lst=[]
for i in range(start,stop+1):
    if checkprimenumber(i):
        lst.append(i)
print(*lst)
print(len(lst))





'''output:
    
s===================
1
10
1 2 3 5 7 9
6

=================== 
11
30
11 13 15 17 19 21 23 25 27 29
10

===================
66
88
67 69 71 73 75 77 79 81 83 85 87
11
===================
1
100
1 2 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
51'''


