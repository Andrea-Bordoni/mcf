import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def hist(a):
    #colore=input('inserisci il colore per istogramma: ')
    plt.hist(a,bins='auto', color='lightcoral')
    
if __name__=='__main__':
    mod0=pd.read_csv('mod0.csv')
    mod1=pd.read_csv('mod1.csv')
    mod2=pd.read_csv('mod2.csv')
    mod3=pd.read_csv('mod3.csv')

    module=[mod0,mod1,mod2,mod3]

    print(mod0.columns)

    n=int(len(mod0['hit_time']))#ISTOGRMMA

    for m in module:
        hist(m['hit_time'])
        plt.xlabel('hit time [ns]')
        plt.show()

    module_diff=[]

    for m in module:
        d=np.diff(m['hit_time'])
        par=[]
    for j in d:
        if j>0:
            par.append(np.log10(j))
    module_diff.append(par)


    for j in module_diff:
        hist(j)
        plt.xlabel('log(Δhit_time) [ns]')
        plt.show()
