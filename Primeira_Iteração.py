import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
# Caso considerássemos a produção natural, levaria 24 horas para voltar à concentração
# inicial, independente da concentração inicial. 
# 5ng/ml por dia produzido por dia de GH.
# V1 seria a velocidade de metabolização do GH pela enzima GHS-R.
# dS é a taxa de variação da concentração de GH no sangue.
Vm = 0.25 # GH METABOLIZADO. Definimos esse parâmetro com base na informação de que demora 24 horas. 
Ve = 0.2 # GH ELIMINADO. 
So = [40]  #Concentração inicial em ng/ml
t= np.linspace(0,24,200)
def func1(Y, t):
    dS= -Vm*Y[0]+(-Ve*Y[0])
    return dS
Y= odeint(func1, So, t)
plt.plot(t, Y)
plt.show()