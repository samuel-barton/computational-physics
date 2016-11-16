from sys import *
import numpy as np
import matplotlib.pyplot as plt
infile = open('periodData.txt', 'r')
outfile = open('junk.dat','w')
times=[]
periods=[]
outfile.write('time \t Period \n')
for line in infile:
	try: 
		t,g,p = line.split()
		times.append(t)
		periods.append(p)
		outfile.write('%12.6f \t %10.6f \n' % (float(t),float(p)) )
	except:
		pass
		
outfile.close()
infile.close()

plt.plot(times,periods)
plt.xlabel('time (s)', fontsize=16)
plt.ylabel('Period (s)', fontsize=16)
plt.text(600, 3.463,r'$\Delta T \sim 1.0$ ms', fontsize=20)
plt.show()
print 'done!'
	
