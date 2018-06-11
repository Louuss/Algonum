from cubic_splines import *
from load_foil import *
from curves_length import *
from math import sqrt
from matplotlib import pyplot as plt
import time as tp

def tp_convert(t):
    h = t//3600
    m = (t%3600)//60
    s = int(t%60)
    return [str(h),str(m),str(s)]

#compute the derivative of the interpolated curve
def interpolation_derivative(X, Y, x):
    A = construct_A(X, Y)
    B = construct_B(X, Y)
    i = identify_interval(X, x)
    second_derivative = second_derivative_Y(A, B)
    return (1/h(X,i))*(Y[i+1]-Y[i])+(h(X,i)/6)*((1-3*(1-zeta(X, x, i))**2)*second_derivative[i]+(3*zeta(X, x, i)**2-1)*second_derivative[i+1])


def pressure_map(ex,ey,ix,iy,resolution):
	#initialize the "clock"
	t0 = tp.time()
	imax = resolution/5
	i = 0

	p_map = np.ones((resolution,resolution))*0.9
	#resolution/5 different lambda values between 0 and 1
	lambda_array = np.linspace(0,1,resolution/5)
	for lbd in lambda_array:
		#upper slice of air associated to current lambda
		fe = lambda x : sqrt(1 + ((1 - lbd)*interpolation_derivative(ex,ey,x))**2)
		#lower slice of air ...
		fi = lambda x : sqrt(1 + (lbd*interpolation_derivative(ix,iy,x))**2)
		length_above = curve_length(simpson, fe, 0, 0.9)
		length_below = curve_length(simpson, fi, 0, 0.9)

		#"g" coordinates are grid's coordinates
		#"r" coordinates are real coordinates
		for xg in range(resolution):
			xr = xg/resolution
			yr_above = interpolation_above(ex, ey, lbd, xr)
			yr_below = interpolation_below(ix, iy, lbd, xr)

			yg_above = int(yr_above*resolution)+resolution//2
			yg_below = int(yr_below*resolution)+resolution//2

			p_map[yg_above,xg] = length_above
			p_map[yg_above+1,xg] = length_above
			p_map[yg_below,xg] = length_below
			p_map[yg_below+1,xg] = length_below

		#print the remaining time	
		i += 1	
		t = (tp.time()-t0)/i
		tp_restant = tp_convert(t*(imax-i))
		print("Il reste "+tp_restant[0]+"h "+tp_restant[1]+"m "+tp_restant[2]+"s")

	return p_map

(dim,ex,ey,ix,iy) = load_foil("boe103.dat")
#change last parameter for better resolution
PM = pressure_map(ex,ey,ix,iy,1000)
plt.imshow(PM, cmap='hot',origin='lower',interpolation='bilinear')
plt.show()