#Aidan Walk
#ASTR 260-001
#HW07.. maybe 06... this number and naming system is getting confusing
#10 March 2021

import numpy as np
import time

def function_to_relax(x, c=None):
    return 1-np.exp(-1*c*x)

def relaxation(start_guess=1, func_to_relax=None,
               func_keyword_args=None, tolerance=1e-6):
    """Function that computes the root via the fixed point
    (relaxation) method. inputs are a starting guess,
    a function to use, any function arguments, and a tolerance
    to exit the function when successive approximations are
    less than this value"""
    guess = start_guess
    for i in range(100):
        if np.abs(guess - func_to_relax(guess, c=func_keyword_args['c'])) <= tolerance:
            break
        guess = function_to_relax(guess, c=func_keyword_args['c'])
    return guess

if __name__ == "__main__":
    print("The solution for part A is:")
    print('{:.6f}'.format(relaxation(func_to_relax=function_to_relax,
                     func_keyword_args={'c':2})))

    print('\n','Calculating the probablility of an empidemic as a function of R0...')
    #loop over r0 values from 0 to 5
    r0_values = np.arange(0, 5.0, 0.01)
    solutions = []
    for r0 in r0_values:
        answer = relaxation(func_to_relax=function_to_relax,
                            func_keyword_args={'c':r0})
        solutions.append(answer)

    #save the output data
    output_textfile = 'problem6_1_data.txt'
    np.savetxt(output_textfile,
               np.array(np.vstack((r0_values, solutions))).T,
               delimiter = ', ', header='R_0, Probability of epidemic',
               fmt = ('%.2f', '%.3e'))
    
    print('Plotting data...')
    import AidanWalk_partB_plot as pB
    pB.savePlot()