#!/usr/bin/python3

d = [[1,2],[2,3]]
print('Delka', len(d))
for x,y in d:
    print(x,y)
    
import collections   
user = collections.namedtuple('user' , 'name passw gender')

co = user('Jan',1234,'male')
print(co._asdict())

se = [1,2,3,4,5]

he = [1,2,3,4,5]

for i in range(len(he)):
    print(he[i])
    
leps = [z for z in range(10,20) if z % 2 == 0]

print(leps)