import matplotlib.pyplot as plt
import numpy as np

def step_euler(y,t,h,f):
    return y + h*f(t,y)

def step_midpoint(y,t,h,f):
    return y + h * f(t + h/2, y + (h/2) * f(t,y))

def step_heun(y,t,h,f):
    tmp = y + h * f(t,y)
    return y + h/2 * (f(t,y) + f(t + h, tmp))

def step_runge_kutta4(y,t,h,f):
    k1= f(t,y)
    k2 = f(t + h/2,  y  + h/2 * k1)
    k3 = f(t + h/2, y + h/2 * k2)
    k4 = f(t + h, y + h * k3)
    return y + h/6 * (k1 + 2*k2 + 2*k3 + k4)

def meth_n_step(y0,t0,N,h,f,meth):
    y = y0
    t = t0
    y_tab = []
    for i in range(N):
        #y_tab = np.append(y_tab,y)
        y_tab.append(y)
        y = meth(y,t,h,f)
        t = t + h
    return np.array(y_tab)

def meth_epsilon(y0,t0,tf,eps,f,meth):
    N = 4
    h = (tf-t0)/N
    solution = meth_n_step(y0,t0,int(N/2),h*2,f,meth)
    solution_double_step = meth_n_step(y0,t0,N,h,f,meth)

    correct = True
    for i in range(len(solution)):
        if(np.linalg.norm(solution[i]-solution_double_step[2*i]) > eps):
            correct = False
            break

    while not(correct):
        solution = solution_double_step
        N = N*2
        h = (tf-t0)/N
        solution_double_step = meth_n_step(y0,t0,N,h,f,meth)
        correct = True
        for i in range(len(solution)):
            if(np.linalg.norm(solution[i]-solution_double_step[2*i]) > eps):
                correct = False

    return solution_double_step


def absolute_error(approx, correct):
    return abs(approx-correct)

def relative_error(approx, correct):
    return abs((approx-correct)/correct)

def absolute_error_array(start, stop, approx_f, f):
    h = (stop - start)*1. / (len(approx_f)-1)
    Err = np.zeros(len(approx_f))
    T = np.arange(start, stop + h, h)
    for i in range(len(approx_f)):
        Err[i] = absolute_error(approx_f[i], f(T[i]))
    return Err

def relative_error_array(start, stop, approx_f, f):
    h = (stop - start)*1. / (len(approx_f)-1)
    Err = np.zeros(len(approx_f))
    T = np.arange(start, stop + h, h)
    for i in range(len(approx_f)):
        Err[i] = relative_error(approx_f[i], f(T[i]))
    return Err


def plot_tangent_field(x0,xf,y0,yf,stepy,stepx,f):
    basex = np.arange(x0, xf, stepx)
    basey = np.arange(y0, yf, stepy)
    X = []
    Y = []
    tx = []
    ty = []
    fx = []
    for i in range(len(basex)):
        for j in range(len(basey)):
            sol = f(basex[i], basey[j])
            tx = tx + [1./((np.sqrt(sol**2+1)))]
            ty = ty + [sol/(abs(sol)*((np.sqrt((1./sol)**2+1))))]
            X.append(basex[i])
            Y.append(basey[j])
    plt.quiver(X,Y,tx,ty)
    plt.show()

def plot_tangent_verify(x0,xf,y0,yf,stepy,stepx,f,eps,meth):
    V = meth_epsilon(y0,x0,xf,eps,f,meth)
    h = (xf-x0)/len(V)
    t0 = x0
    x = []
    for i in range(len(V)):
        x.append(t0)
        t0 += h
    plt.plot(x,V)

    basex = np.arange(x0, xf, stepx)
    basey = np.arange(y0, yf, stepy)
    X = []
    Y = []
    tx = []
    ty = []
    fx = []
    for i in range(len(basex)):
        for j in range(len(basey)):
            sol = f(basex[i], basey[j])
            tx = tx + [1./((np.sqrt(sol**2+1)))]
            ty = ty + [sol/(abs(sol)*((np.sqrt((1./sol)**2+1))))]
            X.append(basex[i])
            Y.append(basey[j])
    plt.quiver(X,Y,tx,ty)
    plt.show()

