import numpy as np
import matplotlib.pyplot as plt
import math
print("Graficador de proba ocurrencia blocking cluster vs gap size")
data1 = np.genfromtxt("proba_block_vsgap_v4", delimiter = '    ')
data2 = np.genfromtxt("proba_block_vs_gap_v6", delimiter = '    ')
data3 = np.genfromtxt("proba_vs_gap_961p_v4", delimiter = '    ')

#gap1=data1[1:,0]
#gap2=data2[1:,0]
gap3=data3[1:,0]

#proba_small_up_v4=data1[1:,2]
#proba_small_up_v6=data2[1:,2]
proba_small_up_961p=data3[1:,2]

#plt.plot(gap1,proba_small_up_v4,'or',label='N= 225  v= 4 m/s')
#plt.plot(gap2,proba_small_up_v6,'ob',label='N= 225 v= 6 m/s')
plt.plot(gap3,proba_small_up_961p,'og',label='N= 961 v= 4 m/s')
plt.xlabel('Gap size(m)')
plt.ylabel('Ocurrence of blocking cluster')
legend = plt.legend(loc='right down', shadow=True)
ax = plt.gca()
ax.set_xlim([0,16.5])
ax.set_ylim([0.55,1])
plt.grid(True)
plt.show()


'''
plt.plot(gap,proba_small_up_v4,'o',label="l2")
plt.figure(1)
l1 = plt.legend(["Small blocking cluster"], loc='right down')
plt.xlabel('Gap size(m)')
plt.ylabel('Ocurrence of blocking cluster')

plt.show()
#plt.savefig('Discharge_g0.jpg')			#Cambiar al cambiar el GAP
axes = plt.gca()


fig, ax = plt.subplots()
#ax.plot(gap, proba_big, 'or', label='Big blocking cluster')
ax.plot(gap, proba_small_up, 'o', label='Small blocking cluster')

# Now add the legend with some customizations.
legend = ax.legend(loc='right middle', shadow=True)

plt.show()


'''
