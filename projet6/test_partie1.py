
from pylab import *
from partie1 import *


#exemple 1 (y' = y/(1+t^2), y(0) = 1)
def test1():
	f = lambda t,y : y/(1+t**2)
	y = 1.
	start = 0.
	stop = 5.
	eps = 0.001

	E = meth_epsilon(y,start,stop,eps,f,step_euler)
	M = meth_epsilon(y,start,stop,eps,f,step_midpoint)
	H = meth_epsilon(y,start,stop,eps,f,step_heun)
	R = meth_epsilon(y,start,stop,eps,f,step_runge_kutta4)

	h = (stop - start)/(len(E)-1)
	t = np.arange(start, stop + h, h)

	h1 = (stop - start)/(len(M)-1)
	t1 = np.arange(start, stop + h1, h1)

	h2 = (stop - start)/(len(H)-1)
	t2 = np.arange(start, stop + h2, h2)

	h3 = (stop - start)/(len(R)-1)
	t3 = np.arange(start,stop + h3, h3)

	plt.clf()
	plt.plot(t,E,color='tab:blue',label="euler")
	plt.plot(t1,M,color='tab:orange',label="midpoint")
	plt.plot(t2,H,color='tab:green',label="heun")
	plt.plot(t3,R,color='tab:red',label="runge_kutta4")

	plt.legend()
	plt.title("Test 1 : y' = y/(1+t^2), y(0) = 1")
	plt.show()



#exemple 2 (y' = [-y2, y1], y(0) = [1,0])
def test2():
	f = lambda t,y : np.array([-y[1], y[0]])
	y = np.array([1., 0])
	start = 0.
	stop = 5.
	eps = 0.001

	E = meth_epsilon(y,start,stop,eps,f,step_euler)
	M = meth_epsilon(y,start,stop,eps,f,step_midpoint)
	H = meth_epsilon(y,start,stop,eps,f,step_heun)
	R = meth_epsilon(y,start,stop,eps,f,step_runge_kutta4)

	h = (stop - start)/(len(E)-1)
	t = np.arange(start, stop + h, h)

	h1 = (stop - start)/(len(M)-1)
	t1 = np.arange(start, stop + h1, h1)

	h2 = (stop - start)/(len(H)-1)
	t2 = np.arange(start, stop + h2, h2)

	h3 = (stop - start)/(len(R)-1)
	t3 = np.arange(start, stop + h3, h3)

	plt.clf()
	plt.plot(t,E,color='tab:blue',label="euler")
	plt.plot(t1,M,color='tab:orange',label="midpoint")
	plt.plot(t2,H,color='tab:green',label="heun")
	plt.plot(t3,R,color='tab:red',label="runge_kutta4")

	plt.legend()
	plt.title("Test 2 : y' = [-y2, y1], y(0) = [1,0]")
	plt.show()


# test erreur (exp)
def test_error():
	f = lambda t,y : y
	y = 1.
	start = 0.
	stop = 3.
	eps = 0.001

	E = meth_epsilon(y,start,stop,eps,f,step_euler)
	M = meth_epsilon(y,start,stop,eps,f,step_midpoint)
	H = meth_epsilon(y,start,stop,eps,f,step_heun)
	R = meth_epsilon(y,start,stop,eps,f,step_runge_kutta4)


	h = (stop - start)/(len(E)-1)
	t = np.arange(start, stop + h, h)

	h1 = (stop - start)/(len(M)-1)
	t1 = np.arange(start, stop + h1, h1)

	h2 = (stop - start)/(len(H)-1)
	t2 = np.arange(start, stop + h2, h2)

	h3 = (stop - start)/(len(R)-1)
	t3 = np.arange(start, stop + h3, h3)


	texp = np.arange(start, stop + eps, eps)
	plt.clf()
	plt.plot(texp,np.exp(texp),color='tab:brown',label="exp")

	plt.plot(t,E,color='tab:blue',label="euler")
	plt.plot(t1,M,color='tab:orange',label="midpoint")
	plt.plot(t2,H,color='tab:green',label="heun")
	plt.plot(t3,R,color='tab:red',label="runge_kutta4")
	plt.legend()
	plt.title("Exponential function")
	plt.show()


	Err_a = absolute_error_array(start, stop, E, np.exp)
	plt.plot(t, Err_a, color='tab:blue', label = "euler")

	Err_a = absolute_error_array(start, stop, M, np.exp)
	plt.plot(t1, Err_a, color='tab:orange', label = "midpoint")

	Err_a = absolute_error_array(start, stop, H, np.exp)
	plt.plot(t2, Err_a, color='tab:green', label = "heun")

	Err_a = absolute_error_array(start, stop, R, np.exp)
	plt.plot(t3, Err_a, color='tab:red', label = "runge_kutta4")

	plt.legend()
	plt.title("Absolute error (exp)")
	plt.show()

	Err_a = relative_error_array(start, stop, E, np.exp)
	plt.plot(t, Err_a, color='tab:blue', label = "euler")

	Err_a = relative_error_array(start, stop, M, np.exp)
	plt.plot(t1, Err_a, color='tab:orange', label = "midpoint")

	Err_a = relative_error_array(start, stop, H, np.exp)
	plt.plot(t2, Err_a, color='tab:green', label = "heun")

	Err_a = relative_error_array(start, stop, R, np.exp)
	plt.plot(t3, Err_a, color='tab:red', label = "runge_kutta4")

	plt.legend()
	plt.title("Relative error (exp)")
	plt.show()


#test champ de vecteurs  (y'=-2xy^2)
def test_tangent_field():
	f = lambda X,Y: -2*X * Y**2
	xmin = -3.
	xmax = 3.
	ymin = -3.
	ymax = 3.
	xstep = 0.15
	ystep = 0.15
	plot_tangent_field(xmin,xmax,ymin,ymax,xstep,ystep,f)

test1()
test2()
test_error()
test_tangent_field()



