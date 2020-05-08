from tkinter import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
import numpy as np
import matplotlib.pyplot as plt

root = Tk()

root.title("Modelado y Simulacion")
root.geometry("300x300")


def graph():
    x = [1, 2, 3]
    y = [2, 4, 1]

    plt.plot(x, y)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('Titulo')

    plt.show()


label_fn = Label(root,text="Funcion")
label_fn.pack()

entry_fn = Entry(root,)
entry_fn.pack()

label_h_steps = Label(root,text="h")
label_h_steps.pack()

entry_h_steps = Entry(root,)
entry_h_steps.pack()

graph_button = Button(root, text = "Graficar", command=graph)
graph_button.pack()

