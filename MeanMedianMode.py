import sys

a=[]
for line in sys.__stdin__:
    a.append(line)

a = a[1].split()
#rint a
sum1 = 0    


#computing the mean
for x in a:
    sum1 = sum1 + int(x)

mean = sum1/float(len(a))
print mean

#computing the median
#typecasting the elements of a 
y=[]
for x in a:
    y.append(int(x))

a=y
a.sort()
#rint a
if len(a) % 2 == 0:   
    i = len(a)/2
    median =  (int(a[i-1])+   int(a[i]))  /float(2) # typcasting 2 with float to output result as float
else:
    i = (len(a)/2) + 1
    median = int(a[i-1])
  
print median

#computing the mode
v=[]
for x in a:
    c = 0
    for y in a:
        if x == y:
            c = c + 1
    v.append(c)

#rint v
if max(v) == 1:
    mode = min(a)
 
else:
    for i in xrange(len(v)):
        if v[i] == max(v):
            mode = a[i]
            
            
print mode  
        
    
    
        


