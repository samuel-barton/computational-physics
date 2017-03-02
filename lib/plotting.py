import matplotlib.pyplot as plt

def darkPlot(x,y,style):
    '''
        This function sets up and does a plot 
        on a dark themed notebook. It removes
        the background color of the plot and
        sets all the outline and text colors 
        to white.
    '''
    fig = plt.figure()
    fig.patch.set_alpha(0.0)
    ax = fig.add_subplot(111)
    ax.plot(x, y,style)
    ax.patch.set_alpha(0.0)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.spines['bottom'].set_color("#FFFFFF")
    ax.spines['top'].set_color("#FFFFFF")
    ax.spines['left'].set_color("#FFFFFF"j)
    ax.spines['right'].set_color("#FFFFFF")
    plt.show()
