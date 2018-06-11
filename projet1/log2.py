def puissance(a,n):
    res = 1
    for i in range(n):
        res = res*a
    return res

for i in range(10,20):
    print "2^%d = %d\n" % (i,puissance(2,i))

def log2(p):
    res = 0
    for i in range(1,10000):
        res = res + float(puissance(-1,i+1))/i
    puiss=puissance(10,p)
    return round(res,p)

def rp(x,p):
    return float(int(x*puissance(10,p)))/puissance(10,p)



    
