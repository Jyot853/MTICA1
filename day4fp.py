'''def bintodecimal(n):
    temp= int(n,2)
    return temp
inp=input()
print(bintodecimal(inp))



output:
    
1111
15

==============
1001010010
594'''

def bintodecimal(n):
    temp= bin(n,[2:])
    return temp
inp=input()
print(bintodecimal(inp))


