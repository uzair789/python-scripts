# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
a=[]
for line in sys.__stdin__:
    a.append(line)

N = int(a[0])
X=a[1].split()
W=a[2].split()
#print N
#print X
#print W

summ = 0
sumW = 0

for i in xrange(len(X)):
    summ = summ + int(X[i])*int(W[i])
    sumW = sumW + int(W[i])

    
mean = summ/float(sumW)
print "%.1f" %mean