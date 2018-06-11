from cubic_splines import *
import matplotlib.pyplot as plt


(dim,ex,ey,ix,iy) = load_foil("boe103.dat")

#------------------------------- Laminar flow above and below the wing -----------#

def laminar_flow(dx, dy, step, interpolation):
    m=[]
    l=0.0
    while (l <= 1.0):
        x = []
        y = []
        for k in np.arange(0.0, 1.0, 0.001):
            x.append(k)
            y.append(interpolation(dx, dy, l, k))
        m.append((x, y))
        l += (1.0/step)
    return m
for (x,y) in laminar_flow(ex, ey, 20, interpolation_above):plt.plot(x,y)
for (x,y) in laminar_flow(ix, iy, 10, interpolation_below):plt.plot(x,y)

plt.title("laminar flow above and below the wing")
plt.show()
