import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('kepler.csv')
print(df.columns)

plt.plot(df['TIME'],df['SAP_FLUX'],color='green')
plt.xlabel('time')
plt.ylabel('flux')
plt.show()
"""
plt.plot(df['TIME'],df['SAP_FLUX'],'o',color='red')
plt.xlabel('time')
plt.ylabel('flux')
plt.show()

plt.errorbar(df['TIME'],df['SAP_FLUX'],yerr=df['SAP_FLUX_ERR'],fmt='o',color='green')
plt.xlabel('time')
plt.ylabel('flux')
plt.show()

"""
min=df['SAP_FLUX'].idxmin()
"""
plt.plot(df['TIME'].iloc[min-1500:min+1500],df['SAP_FLUX'].iloc[min-1500:min+1500],'o',color='pink')
#plt.savefig("kepler_zoom.pdf")
plt.axvline(df['TIME'].iloc[min])
plt.xlabel('time')
plt.ylabel('flux')
plt.show()

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(df['TIME'],df['SAP_FLUX'])
ins_ax=ax.inset_axes([0.8, 0.8, 0.2, 0.2])
ins_ax.errorbar(df['TIME'].iloc[min-1500:min+1500],df['SAP_FLUX'].iloc[min-1500:min+1500],yerr=df['SAP_FLUX_ERR'].iloc[min-1500:min+1500])
plt.savefig("kepler_zoom2.pdf")
plt.show()
"""


