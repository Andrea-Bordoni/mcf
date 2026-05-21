import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('exo.csv', comment='#')
#print(df.columns)

solar_system_n=['Mercury','Venus','Mars','Earth','Jupiter','Saturn','Uranus','Neptune']
solar_system_mt=[0.055,0.815,1,0.107,317.8,95.1,14.5,17.1]
solar_system_mj=[m / 317.8 for m in solar_system_mt]
solar_system_p=[88,225,365,687,4329,10751,30664,60148]

solar_system={'name':solar_system_n,'mass':solar_system_mj,'period':solar_system_p}
ss_df=pd.DataFrame(solar_system)
#print(ss_df.columns)
"""
plt.scatter(df['pl_orbper'], df['pl_bmassj'],color='red', label='esopianeti')
plt.scatter(ss_df['period'],ss_df['mass'],color='yellow', label='sistema solare')
plt.xlabel('orbital period [days]')
plt.ylabel('planet mass [jupiter mass]')
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()

semiax2=df['pl_orbsmax']**2
rm=semiax2/df['st_mass']
semiax_solar=[0.387,0.723,1.000,1.524,5.203,9.555,19.201,30.058]
semiax_solar2=[r*r for r in semiax_solar]
plt.scatter([p/365 for p in df['pl_orbper']],rm, color='blue',label='exoplanet')
plt.scatter([p/365 for p in solar_system_p],semiax_solar2,color='red',label='solar system')
plt.xlabel('period[years]')
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
plt.show()
"""
n=len(df['discoverymethod'])
radial=np.zeros(n)
transit=np.zeros(n)
for j in range(n):
    if(df['discoverymethod'].iloc[j]=='Radial Velocity'):
        radial[j]=1

    else:
        radial[j]=0

for j in range(n):
    if(df['discoverymethod'].iloc[j]=='Transit'):
        transit[j]=1
    else:
        transit[j]=0

masst=df['pl_bmassj']*transit
massrv=df['pl_bmassj']*radial
p_t=df['pl_orbper']*transit
p_rv=df['pl_orbper']*radial

"""
plt.scatter(p_t,masst, color='royalblue',label='transit')
plt.scatter(p_rv,massrv,color='darkorange',label='Radial Velocity')
plt.scatter(ss_df['period'],ss_df['mass'],color='seagreen',label='solar system')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Period [days]')
plt.ylabel('planet mass [mj]')
plt.legend(fontsize=14)
plt.show()
"""

#ISTOGRAMMA
"""
plt.hist(massrv, bins=int(np.sqrt(n)),color='royalblue',alpha=0.7,label='Transit')
plt.hist(masst, bins=int(np.sqrt(n)),color='yellow',alpha=0.4,label='Radial Velocity')
plt.legend(fontsize=10)
plt.xlabel('palnet mass (mj)')
plt.ylabel('number of planets')
plt.show()


plt.hist([np.log(m) for m in massrv if m>0],bins=int(np.sqrt(n)),color='blue',alpha=0.4,label='radial velocity')
plt.hist([np.log(m) for m in masst if m>0],bins=int(np.sqrt(n)),color='green',alpha=0.5,label='transit')
plt.xlabel('log(mj)')
plt.legend(fontsize=10)
plt.show()
"""
masst_log=[np.log(m) for m in masst if m>0]
massrv_log=[np.log(m) for m in massrv if m>0]
pt_log=[np.log(m) for m in p_t if m>0]
prv_log=[np.log(m) for m in p_rv if m>0]

fig=plt.figure()
gs=fig.add_gridspec(2,2, hspace=0,wspace=0)
ax1=fig.add_subplot(gs[0,0])
ax2=fig.add_subplot(gs[1,0],sharex=ax1)
ax3=fig.add_subplot(gs[1,1],sharey=ax1)

ax2.scatter(p_t,masst,color='blue',label='Transit')
ax2.scatter(p_rv,massrv,color='red',label='Radial Velocity')
ax1.hist(pt_log,bins=int(np.sqrt(n)),color='green',label='Transit')
ax1.hist(prv_log,bins=int(np.sqrt(n)),color='red',label='Radial Velocity')
ax3=plt.hist([np.log(m) for m in massrv if m>0],bins=int(np.sqrt(n)),color='blue',alpha=0.4,label='radial velocity')
ax3=plt.hist([np.log(m) for m in masst if m>0],bins=int(np.sqrt(n)),color='green',alpha=0.5,label='transit')
plt.legend(fontsize=10)
plt.show()
