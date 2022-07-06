import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


parameters = {'axes.labelsize': 25,
          'axes.titlesize': 35,
          'xtick.labelsize': 25,
          'ytick.labelsize': 25}
plt.rcParams.update(parameters)


data = {
'Experiment': ['ALEPH','DELPHI','L3','OPAL','LEP2','CDF','D0','Tevatron','ATLAS','LHCb','LHC','World Avg','CDF 2022'], 
'Mass':       [80.440,  80.336, 80.270, 80.415, 80.376, 80.389, 80.383, 80.387, 80.370, 80.354, 80.366, 80.377, 80.4335], 
'Error':      [0.051, 0.067, 0.055, 0.052, 0.033, 0.019, 0.023, 0.016, 0.019, 0.032,  0.017,  0.012,  0.0094]
}  

data2 = {
'Experiment': ['ALEPH','DELPHI','L3','OPAL','LEP2','CDF','D0','Tevatron','ATLAS','LHCb','LHC','CDF 2022'],
'Mass':       [80.440,  80.336, 80.270, 80.415, 80.376, 80.389, 80.383, 80.387, 80.370, 80.354, 80.366,  80.4335], 
'Error':      [0.051, 0.067, 0.055, 0.052, 0.033, 0.019, 0.023, 0.016, 0.019, 0.032,  0.017,  0.0094]
}
#df = pd.DataFrame(data)

df2 = pd.DataFrame(data2)
df2  = df2[::-1] # reverse the data set


error = ((1/(df2['Error']*df2['Error'])).sum())
error = math.sqrt(1/error)
std = error

mean = pd.DataFrame()
mean = ((df2['Mass']/(df2['Error']*df2['Error'])).sum())/(((1/df2['Error'])**2).sum())
print("PDG World Average : 80.377 +/- 0.012")
print("This World Average :", mean, " +/- ", std)


fig,ax=plt.subplots(figsize=(8, 10),sharex=True)
plt.xlim(xmin=(df2['Mass']-df2['Error']).min()-.02,xmax=(df2['Mass']+df2['Error']).max()+.09)
plt.errorbar(df2['Mass'],df2['Experiment'],xerr=df2['Error'],fmt='o',linestyle='',label='Data',color='black')
plt.fill_betweenx(df2['Experiment'],(df2['Mass'].mean()-.012)*np.ones(len(df2)),(df2['Mass'].mean()+.012)*np.ones(len(df2)),color='orange',label='World uncertainity')
plt.fill_betweenx(df2['Experiment'],(df2['Mass'].mean()-std)*np.ones(len(df2)),(df2['Mass'].mean()+std)*np.ones(len(df2)),color='yellow',label='This world uncertainity')
plt.plot(80.377*np.ones(len(df2)),df2['Experiment'],linestyle='--',label='World Average',color='brown')
plt.plot(df2['Mass'].mean()*np.ones(len(df2)),df2['Experiment'],linestyle='--',label='This World Average',color='blue')

plt.legend()
fig.tight_layout()
plt.savefig("wmass_plot.png")
plt.show()
