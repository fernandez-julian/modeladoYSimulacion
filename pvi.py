import numpy as np
import matplotlib.pyplot as plt


def f(t, x):#funcion a resolver
    #return 2*t
    return t-x+2

def euler (x0, t0, tf, h, f):
    lista_t  = []
    lista_x = []
    x = x0
    t = t0
    while t < tf + h:
        lista_t.append(t)
        lista_x.append(x)
        x += h * f(t, x)
        t += h
        #print("valor de t= {}".format(t))
    plt.plot(lista_t, lista_x)
    plt.show()

def euler_mejorado (x0, t0, tf, h, f):
    lista_t  = []
    lista_x_predictor = []
    lista_x_corrector = []
    x_predictor = x0
    x_corrector = x0
    t = t0
    while t < tf + h:
        lista_t.append(t)
        lista_x_predictor.append(x_predictor)
        lista_x_corrector.append(x_corrector)
        x_predictor += h * f(t, x_predictor)
        x_corrector += ((h/2) * (f(t, x_corrector) + f(t+h, x_predictor)))
        t += h
    plt.plot(lista_t, lista_x_predictor)
    plt.plot(lista_t, lista_x_corrector)
    plt.show()

def rungeKutta (x0, t0, tf, h, f):
    lista_t  = []
    lista_x = []
    x = x0
    t = t0
    while t < tf + h:
        lista_t.append(t)
        lista_x.append(x)
        alpha1 = f(t, x)
        alpha2 = f((t+(h/2)), (x+(alpha1*h/2)))
        alpha3 = f((t+(h/2)), (x+(alpha2*h/2)))
        alpha4 = f(t+h, (x + (alpha3*h)))
        x += (h/6) * ( alpha1 + (2*alpha2) + (2*alpha3) + alpha4)
        t += h
    plt.plot(lista_t, lista_x)
    plt.show()

#euler(0, 0, 1, 0.25, f)
#euler_mejorado(2, 0, 1, 0.1, f)
#rungeKutta(2, 0, 1, 0.1, f)