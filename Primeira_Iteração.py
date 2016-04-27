import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from numpy import linspace
# Caso considerássemos a produção natural, levaria 24 horas para voltar à concentração
# inicial, independente da concentração inicial. 
# 5ng/ml por dia produzido por dia de GH.
# V1 seria a velocidade de metabolização do GH pela enzima GHS-R.
# dS é a taxa de variação da concentração de GH no sangue.
V1 = 0.04 #Precisamos definir esse valor
So = 40  #Concentração inicial em ng/ml
t= np.linspace(0,24,200)
def func1(Y, t):
    dS= -V1*So
    return dS
Y= odeint(func1, So, t)
plt.plot(t, Y)
plt.show()