def getParams(string
#
#	READ IN RUN PARAMETERS 
#	and Define variables needed   
parser = argparse.ArgumentParser()

# define all options:
parser.add_argument('--filename', dest='filename', \
action="store", help='output filename', default="junk.dat")

parser.add_argument('--v_initial', dest='v', type=float, \
default=0.0, help='initial velocity')

parser.add_argument('--dt', dest='dt', help='time steps', \
action='append', nargs='*')	# the append action makes a list. 

#now read from command line 
input = parser.parse_args()
#define the variables we need 
filename=input.filename
# set initial velocity:
v=input.v 	
#save initial velocity for later use (for multiple runs):
vinitial = v 
# saves dt values as a string list called timeSteps:
timeSteps = input.dt