import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
# Na segunda iteração, temos que considerar o GH injetado e também que a velocidade de
# metabolização e eliminação dependem dessa quantidade. 
# Pico de concentração de GH de 3(intravenoso) a 4 horas(subcutâneo).
# (Na-Ma)*At*(1-(Tt/Tc))
# (Nt-Mt)*Tt*((At/Ac)-1)
So = [40]  #Concentração inicial em ng/ml
Vd= #Velocidade de distribuição do GH no sangue. Aumenta a concentração do mesmo.
GH= 20 # em unidade IU
GHc= 8 #GH crítico, a partir disso o fígado não consegue metabolizar e a eliminação 
# acontece.
Vm= 0.15*((1-(GH/GHc))**2) #Criar uma função que quando o GH injetado é igual ou maior que o critico
# a metabolização é a máxima, ou seja, não cresce mais.
Ve= 0.01*(((GH/GHc)-1)**2) #Criar uma função que quando o GH injetado é igual ou maior que o crítico
# a eliminação começa a aumentar.
t= np.linspace(0,24,200)
def func1(Y, t):
    dS= -Vm*Y[0]+(-Ve*Y[0])+Vd*Y[0]
    return dS
Y= odeint(func1, So, t)
plt.plot(t, Y)
plt.show()
