import math
import numpy
def rp (r,p):
        if(r==0):
                return 0
        pt=10**math.floor(p-numpy.log10(math.fabs(r)))
        return (math.floor(r*pt) + ((r * pt * 10) % 10) // 5) / pt

def sum(a,b,p):
    return rp(rp(a,p) + rp(b,p), p)

def mul(a,b,p):
    return rp(rp(a,p) * rp(b,p), p)
def erel(r, m, p):
        if(r==0):
                return 0
        return rp(math.fabs( ( r - m ) / r), p)

def erel_sum(x,y,p):
        return erel(x+y, sum(x,y,p),p)
def erel_mul(x,y,p):
        return erel(x*y, mul(x,y,p),p)

def log2(q):
        cur=0
        nrm=0
        n=10.0**q
        while(n>0):
                cur=sum(cur, ((-1)**(n+1))/n, q)
                nrm=nrm + ((-1)**(n+1))/n
                n=n-1
        return (cur, nrm, erel(nrm, cur, q))
#print sum(3.141592658,10507.1823, 6), 3.141592658+10507.1823
