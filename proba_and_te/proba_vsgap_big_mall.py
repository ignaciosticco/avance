import numpy as np
import matplotlib.pyplot as plt
import math
print("Plot Proba vs gap")

data1 = np.genfromtxt('proba_block_vsgap_v4', delimiter = '    ')
gap1=data1[:,0]
proba_big=data1[:,1]
gap2=data1[1:,0]
proba_small_up=data1[1:,2]

plt.figure(1)
plt.plot(gap1,proba_big,linestyle='',marker='o',label='Big')
plt.plot(gap2,proba_small_up,linestyle='',marker='o',label='Small')
#plt.axvline(1.2,linewidth=2, color='k', linestyle='-')
plt.legend(loc='center right')
plt.xlabel('Gap size (m)')
plt.ylabel('Ocurrence of blocking cluster')

axes = plt.gca()
plt.grid(True)
axes.set_xlim([-0.2,7.3])
axes.set_ylim([-0.1,1])
plt.show()
