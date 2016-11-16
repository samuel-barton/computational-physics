from sys import *
#from pylab import *
infile = open('periodData.txt', 'r')
times=[]
for line in infile:
	try: 
		if(len(line.split())==3):
			t,g,p = line.split()
		elif(len(line.split())==2):
			t,g = line.split()
		times.append(float(t))
	except:
		pass
		
infile.close()

print times	
