from numpy import matrix
from numpy import linalg

A = matrix([[1,2,3],[2,7,4]])
B = matrix([[1,-1],[0,1]])
C = matrix([[5,-1],[9,1],[6,0]])
D = matrix([[3,-2,-1],[1,2,3]])

u = matrix([[6,2,-3,5]])
v = matrix([[3,5,-1,4]])
w = matrix([[1],[8],[0],[5]])

magn = 0
for n in range (u.shape[1]):
    magn = magn + u[0,n]**2

magn = magn**.5

print "1.1)", A.shape[0],"x",A.shape[1]
print "1.2)", B.shape[0],"x",B.shape[1]
print "1.3)", C.shape[0],"x",C.shape[1]
print "1.4)", D.shape[0],"x",D.shape[1]
print "1.5)", u.shape[0],"x",u.shape[1]
print "1.6)", w.shape[0],"x",w.shape[1]
print " "
print "2.1)", u + v
print "2.2)", u - v
print "2.3)", 6*u
print "2.4) Not defined"
print "2.5)", magn

print " "
print "3.1) Not defined"
print "3.2)", A - C.T
print "3.3)", C.T + 3*D
print "3.4)", B*A
print "3.5) Not defined"
print "3.6) Not defined"
print "3.7)", C*B
print "3.8)  ??"
print "3.9)", A * A.T
print "3.10)", D.T * D
