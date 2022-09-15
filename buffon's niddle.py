import math
import random

n=int(input("시행횟수:"))
l=int(input("바늘길이:"))
d=int(input("평행선 사이 거리:"))
res=0

for i in range(n):
    theta=(math.pi)*random.random()
    if l*math.sin(theta)/2 >= (d/2)*random.random():
        res+=1

p=res/n
print((2*l)/(d*p))
