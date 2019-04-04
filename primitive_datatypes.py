# Primitive Data types

a = 5
print("The value of a is ",end = ' ')
print(a)

b = 7.0
print(type(b))


c = 'Hello World, I am new to Python'
print(c)

d = True
print(type(d))
print(d)


# Non-primitive datatype (Python Collections)

l = [1,2,3,4]
print(type(l))

print(c.split(" "))
# Append to books_list

l.append(7)
print(l)

l.remove(2)
print(l)

del l[0]
print(l)

del l[1]
print(l)
#for element in l: print(element,end = ',')


l1 = [1,1,3,3,5,6,7]
l2 = [3,4,5,7,9,9,9]

s1 = set(l1)
print('Set is')
print(s1)

s2 = set(l2)
print(s2)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

# Dictionary

d1 = {1:"Vinay",2:"Nitin"}
print(d1)
print(d1.keys())
#print(d1[3])
print(d1.get(3))


l3 = list(range(0,5))
print(l3)

for i in l3:
    print(i)

#Print only even numbers here:

for i in l3:
    if i%2 != 0:
        print(i)

#Add even numbers:

s=0
for i in l3:
    if i%2 ==0:
        s=s+i
print("sum is ",end='')
print(s)

def evenSum(ub,lb):
    l3 = list(range(ub,lb))
    s=0
    for i in l3:
        if i%2 ==0:
            print(i)
            s=s+i
    return s

r = evenSum(5,9)
print(r)

def sq(i): return i*i

def evenSum(func,ub,lb):
    l3 = list(range(ub,lb))
    s = 0
    for i in l3:
        if i%2 ==0:
            s=s+func(i)
    return s


r = evenSum(sq,5,9)
print(r)

# Map Filter and Reduce
# Lambda Function - Anonymous function

x = lambda x: x*x

print(x(5))


def ntimesGivenNumber(n):
    return lambda a:a*n

doubler = ntimesGivenNumber(2)
final_value = doubler(11)
print(final_value)

tripler = ntimesGivenNumber(3)
final_value = tripler(11)
print(final_value)


# Lazy execution
from functools import reduce
l5 = list(range(0,5))
filt_list = filter(lambda x:x%2 ==0,l5)
#print(list(filt_list))
map_list = map(lambda x:x*x,list(filt_list))
#print(list(map_list))
reduce_list = reduce(lambda x,y:x+y,map_list)
print(reduce_list)

# OS and directories
import os
local_dir = 'C:\\Users\\Kisho\\Downloads\\'
specific_dir = 'data-master\\data-master\\retail_db\\order_items\\'
bool = os.path.exists(local_dir+specific_dir)
print(os.listdir(local_dir+specific_dir))
print(bool)
fopen = open(local_dir+specific_dir+'part-00000')
fread = fopen.read()
print(type(fread))
print(fread.split("\n")[0])
flines = fread.split("\n")
print(flines[-1:])
flines = flines[:-1]
print(len(flines))
#cat part-00000 | Measure-Object -line

# Filter for order_id and sum the net revenue

ffilt = filter(lambda x:int(x.split(",")[1])==68883,flines)
fmap = map(lambda x:float(x.split(",")[4]),ffilt)
freduce = reduce(lambda x,y:x+y,fmap)
print(freduce)

# Let's wrap this up in a neat function

def calculateRevenueForOrderID(orderid):
    ffilt = filter(lambda x:int(x.split(",")[1])==orderid,flines)
    fmap = map(lambda x:float(x.split(",")[4]),ffilt)
    freduce = reduce(lambda x,y:x+y,fmap)
    return freduce

revenue = calculateRevenueForOrderID(10)
print(revenue)
