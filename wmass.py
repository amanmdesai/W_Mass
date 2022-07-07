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


data3 = {
'Experiment': ['ALEPH','DELPHI','L3','OPAL','CDF','D0','ATLAS','LHCb','CDF 2022'],
'Mass':       [80.440,  80.336, 80.270, 80.415, 80.389, 80.383, 80.370, 80.354,  80.4335], 
'Error':      [0.051, 0.067, 0.055, 0.052, 0.019, 0.023,  0.019, 0.032, 0.0094]
}




df = pd.DataFrame(data2)
df  = df[::-1] # reverse the data set


error = ((1/(4*df['Error']*df['Error'])).sum())
error = math.sqrt(1/error)
std = error
print(std)
#std2 = (df['Mass'] - df['Mass'].mean())**2
#std2 = (std2/(len(df)-1)).sum()
#print(std2)

mean = pd.DataFrame()
mean = ((df['Mass']/(df['Error']*df['Error'])).sum())/(((1/df['Error'])**2).sum())
print("PDG World Average : 80.377 +/- 0.012")
print("This World Average :", mean, " +/- ", std)


fig,ax=plt.subplots(figsize=(8, 10),sharex=True)
plt.xlim(xmin=(df['Mass']-df['Error']).min()-.02,xmax=(df['Mass']+df['Error']).max()+.09)
plt.errorbar(df['Mass'],df['Experiment'],xerr=df['Error'],fmt='o',linestyle='',label='Data',color='black')
plt.fill_betweenx(df['Experiment'],(df['Mass'].mean()-.012)*np.ones(len(df)),(df['Mass'].mean()+.012)*np.ones(len(df)),color='orange',label='World uncertainity')
plt.fill_betweenx(df['Experiment'],(df['Mass'].mean()-std)*np.ones(len(df)),(df['Mass'].mean()+std)*np.ones(len(df)),color='yellow',label='This world uncertainity')
plt.plot(80.377*np.ones(len(df)),df['Experiment'],linestyle='--',label='World Average',color='brown')
plt.plot(df['Mass'].mean()*np.ones(len(df)),df['Experiment'],linestyle='--',label='This World Average',color='blue')
plt.xlabel('Mass of W boson')
plt.ylabel('Experiment')
plt.legend()
fig.tight_layout()
plt.savefig("wmass_plot.png")
plt.savefig("wmass_plot.pdf")
plt.show()
