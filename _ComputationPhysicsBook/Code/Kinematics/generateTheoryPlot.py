import numpy as np
import matplotlib.pyplot as plt



vt = 1.0
g = 1.0
 
t = np.linspace(0,6,500)
a = vt*(1-np.exp(-g*t/vt))
fig = plt.figure(figsize=(9,5), dpi=100)
axes = fig.add_axes([0.15, 0.15, 0.8, 0.7])

axes.set_ylabel('Speed', fontsize=20)
axes.set_xlabel('time', fontsize = 20)
plt.xticks([0, 1.0, 2.0], ('0', r'$\tau$', r'$2\tau$'), fontsize=16 )
plt.yticks([0, 0.63, 1.0 - np.exp(-2.0), 1.0], ('0', r'$0.63V_{\mathrm{t}}$', r'$0.86V_{\mathrm{t}}$', r'$V_{\mathrm{t}}$'), fontsize=16)
plt.ylim(0,1.2)
plt.plot(t, a)
plt.plot([0,6],[1.0, 1.0], '--k')
plt.show()
plt.savefig('theory.pdf', dpi=600)