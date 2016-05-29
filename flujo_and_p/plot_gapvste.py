import numpy as np
import matplotlib.pyplot as plt
import math
print("Plot gap vs te")
#from publib import set_style, fix_style
#set_style('article')        # before the first plot

data1 = np.genfromtxt('gap_vs_te_v4_20x20.txt', delimiter = '   ')
gap1=data1[:,0]
te1=data1[:,1]
yerr1=data1[:,2]
for i in range(0,len(yerr1)):
	if (i+1)%3 != 0:
		yerr1[i]=0


data2 = np.genfromtxt('gap_vs_te_v8.txt', delimiter = '   ')
gap2=data2[:,0]
te2=data2[:,1]
yerr2=data2[:,2]
for i in range(0,len(yerr2)/2):
	yerr2[2*i]=0

'''
data2 = np.genfromtxt('gap_vs_te_30x30.txt', delimiter = '   ')
gap2=data2[:,0]
te2=data2[:,1]/529
yerr2=data2[:,2]/529
for i in range(0,len(yerr2)/2):
	yerr2[2*i]=0


'''
data3 = np.genfromtxt('gap_vs_te_40x40.txt', delimiter = '   ')
gap3=data3[:,0]
te3=data3[:,1]
yerr3=data3[:,2]
for i in range(0,len(yerr3)/2):
	yerr3[2*i]=0


plt.figure(1)
#plt.errorbar(gap1,te1,yerr1,linestyle='',marker='o',label='vd= 4 m/s ')
#plt.errorbar(gap2,te2,yerr2,linestyle='',marker='o',label='vd= 8 m/s')
plt.errorbar(gap3,te3,yerr3,linestyle='',marker='o',color='green',label='N= 961')
#plt.axhline(y=40, xmin=0, xmax=21, linewidth=2, color = 'green')  #linea horizontal
#plt.axvline(1.2,linewidth=2, color='k', linestyle='-')
plt.legend(loc=4)
plt.xlabel('Gap size (m)')
plt.ylabel('Evacuation Time (s)')#, fontsize=30)

axes = plt.gca()
#plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.grid(True)
#fix_style('article')
axes.set_xlim([-0.1,16.5])
#axes.set_ylim([0.1,0.48])
plt.show()
