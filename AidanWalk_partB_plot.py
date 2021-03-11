#Aidan Walk
#ASTR 260-001
#HW07, maybe 06
#10 March 2021
 
import matplotlib.pyplot as plt
import numpy as np

partB_data = np.loadtxt('problem6_1_data.txt', delimiter=',')

def savePlot():
    '''Plots probalility of an epidemic as a function of R0, 
    AidanWalk_HW07_1.py must properly generate problem6_1_data.txt to work'''
    plt.plot(partB_data[:,0], partB_data[:,1], color='black')
    plt.ylabel('Probablility of Epidemic')
    plt.xlabel('R0')
    plt.title("Probablility of Epidemic as a F'n of R0")
    
    plt.savefig('AidanWalk_1B_plot.png')
    print('Plot saved to AidanWalk_1B_plot.png')
