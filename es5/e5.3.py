import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from reco import hit
from hit import hist

modules=['mod0.csv','mod1.csv','mod2.csv','mod3.csv']

def read_csv(a):
    return pd.read_csv(a)

mod=[]
for j in modules:
    mod.append(read_csv(j))

n=len(mod[0]['hit_time'])

events_mod0=[]
events_mod1=[]
events_mod2=[]
events_mod3=[]

events=[events_mod0,events_mod1,events_mod2,events_mod3]


for j in range(len(mod)):
    df=mod[j]
    for i in range(len(df)):
        h=hit(df['mod_id'].iloc[i],df['det_id'].iloc[i],df['hit_time'].iloc[i])
        events[j].append(h)           
           
tot=[]

for k in events:
    tot=tot+k

tot.sort(key=lambda h: h.time)



time=[h.time for h in tot]
diff=np.diff(time)

hist(diff)
plt.xlabel('delta t hit time [ns]')
plt.show()
