import math
import numpy as np
import partie1 as p1
import matplotlib.pyplot as plt

t = 0

g = 9.81
l = 1

#equadiff:
def pendule1():
        return lambda t, Y: np.array([(-math.sin(Y[1])* g/l), Y[0]])

def pendule_simple(theta0):
        t = [0]
        Y = [np.array([0, theta0])]
        h = 0.01
        for i in range(500):
                t += [t[-1] + h]
                Y += [p1.step_rungekutta(Y[-1],t[-1],h,pendule1())]


        plt.plot(t, [i[1] for i in Y])
        plt.show()

def frequency(theta0):
        h = 0.01
        t = h
        Y = p1.step_rungekutta(np.array([0, theta0]),t,h,pendule1())

        while (theta0 - Y[1] > 10**-4):
                Y = p1.step_rungekutta(Y, t, h, pendule1())
                t += h
        return t

theta = math.pi/8
#print(frequency(theta))
#pendule_simple(theta)


# PENDULE A DEUX MAILLONS

l1 = 1
l2 = 1
m1 = 1
m2 = 1

def pendule2():
        """on definit l'equation sous forme de lambda expression"""
        return lambda T,Y: np.array([\
                                     (-g*(2*m1+m2)*math.sin(Y[2])-m2*g*math.sin(Y[2]-2*Y[3])-2*math.sin(Y[2]-Y[3])*m2*(Y[1]**2*l2+Y[0]**2*l1*math.cos(Y[2]-Y[3]))) / (l1*(2*m1+m2-m2*math.cos(2*Y[2]-2*Y[3]))),\
                                     (2*math.sin(Y[2]-Y[3])*(Y[0]**2*l1*(m1+m2)+g*(m1+m2)*math.cos(Y[2])+Y[1]**2*l2*m2*math.cos(Y[2]-Y[3]))) / (l2*(2*m1+m2-m2*math.cos(2*Y[2]-2*Y[3]))),\
                                     Y[0],\
                                     Y[1]\
        ])

def show_mvt_double_pendule(theta1, theta2) :
        t = [0]
        x1 = [l1*np.sin(theta1)]
        y1 = [-l1*np.cos(theta1)]
        x2 = [x1[0] + l2*np.sin(theta2)]
        y2 = [y1[0] - l2*np.cos(theta2)]
        Y = [np.array([0, 0, theta1, theta2])]
        h = 0.01
        u1 = [l1*np.sin(theta1+0.01)]
        v1 = [-l1*np.cos(theta1+0.01)]
        u2 = [u1[0] + l2*np.sin(theta2-0.01)]
        v2 = [v1[0] - l2*np.cos(theta2-0.01)]
        V = [np.array([0, 0, theta1+0.01, theta2-0.01])]

        for i in range(5000):
                t += [t[-1] + h]
                Y += [p1.step_rungekutta(Y[-1],t[-1],h,pendule2())]
                x1 += [l1*np.sin(Y[i][2])]
                y1 += [-l1*np.cos(Y[i][2])]
                x2 += [x1[i] + l2*np.sin(Y[i][3])]
                y2 += [y1[i] - l2*np.cos(Y[i][3])]
                V += [p1.step_rungekutta(V[-1],t[-1],h,pendule2())]
                u1 += [l1*np.sin(V[i][2])]
                v1 += [-l1*np.cos(V[i][2])]
                u2 += [u1[i] + l2*np.sin(V[i][3])]
                v2 += [v1[i] - l2*np.cos(V[i][3])]
                plt.figure("Figure")	
                plt.plot(x2, y2, "b", label="Initial")
                plt.plot(u2, v2, "r", label="Leger decalage")
                plt.legend()
                plt.show()

#show_mvt_double_pendule(math.pi/2, 0)

a = (l1/g)**(1/2)

def first_flip_time(theta1, theta2):
        t = 0
        Y = np.array([0, 0, theta1, theta2])
        h = 0.01
        while t < 10000*a and (abs(Y[3]) > 0.001 or abs(Y[1]) < 1):
                t += h
                Y = p1.step_rungekutta(Y,t,h,pendule2())
        return t

def draw_flip_graph(N = 7):
        M = np.array([[0 for j in range(N)] for i in range(N)])
        h = 6/(N-1)
        for i in range(N):
                tmp = []
                theta1 = i * h - 3
                for j in range(N):
                        theta2 = j * h - 3
                        print((i*N + j )*100/(N**2),"%")
                        #tmp.append(theta1 + theta2)
                        tmp.append(first_flip_time(theta1, theta2))
                M[i] = np.copy(tmp)
        print(M)
        plt.clf()
        plt.title("Temps de retournement en fonction des angles initiaux")
        plt.imshow(M, cmap='viridis')
        plt.colorbar()
        plt.show()

draw_flip_graph()
