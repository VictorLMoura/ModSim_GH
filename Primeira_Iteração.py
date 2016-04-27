import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Caso considerássemos a produção natural, levaria 24 horas para voltar à concentração
# inicial, independente da concentração inicial. 
# 5ng/ml por dia produzido por dia de GH.
# V1 seria a velocidade de metabolização do GH pela enzima GHS-R.
# dS é a taxa de variação da concentração de GH no sangue.
V1 = 0
def func1():
    dS=