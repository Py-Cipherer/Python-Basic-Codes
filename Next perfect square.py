import math
def next_perfect_sq(a):
    if a==1 or a==0:
        return (a+1)**2
    if (a+1)%(math.sqrt(a))==1:
        return (math.sqrt(a)+1)**2
    return -1
print(next_perfect_sq(155))
print(next_perfect_sq(144))
print(next_perfect_sq(179))
