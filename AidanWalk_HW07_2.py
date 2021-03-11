#Aidan Walk
#ASTR 260-001
#HW07.. maybe 06
#10 March 2021

#Problem 2
 
import numpy as np

#define global variables bc I am going to use them in just about every function
global G, M, m, R, omega
G = 6.674e-11 #m^3 kg^-1 s^2, Newtons gravity constant
M = 1.989e30 #kg, Mass of sun
m = 5.972e24 #kg, Mass of Earth
R = 1.496e11 #m, distance from the Sun to Earth 
omega = 1.991e-7 #s^-1, angular fq 

def function(r, position=None):
    firstTerm = G*M/r**2
    secondTerm = G*m / (R-r)**2
    rightSide = omega**2*r
    
    if position=='l2':
        answer = (firstTerm + secondTerm) - rightSide
    elif position=='l1':
        answer = (firstTerm - secondTerm) - rightSide
    return answer

def analyticalDerivativeF(r, position=None):
    firstTerm = -2*G*M / r**3
    secondTerm = 2*G*M / (R-r)**3
    rightSide = omega**2
    
    if position=='l2':
        answer = (firstTerm + secondTerm) - rightSide
    elif position=='l1':
        answer = (firstTerm - secondTerm) - rightSide
    return answer

def newtonsMethod(point=None):
    maxIterations = 1000000
    guess = 1e11
    for i in range(maxIterations):
        guess = guess - function(guess, position=point) / \
                        analyticalDerivativeF(guess, position=point)
        if i == maxIterations/2:
            print('...Half way there...')
    return guess

def secant(point):
    #two points initial interval
    p2=1e11; p1=1.8e11
    maxIterations = 1000
    
    for i in range(maxIterations):
        x0 = p1 - function(p1, position=point) * \
             ( (p2-p1)/(function(p2, position=point)-function(p1, position=point)) )
    
        if function(p1, position=point)*function(p2, position=point) < 0:
            p1 = p1
            p2 = x0
        elif function(p1, position=point)*function(p2, position=point) > 0:
            p1 = x0
            p2 = p2
        else:
            print('function(p1)*function(p2) = 0 at point:', point)
            break
    return x0

if __name__ == '__main__':
    #newtons method 
    print("\nNEWTON'S METHOD:")
    print("\tCalculating for L1...")
    l1distFromEarth_newt = newtonsMethod('l1')
    print("\tCalculating for L2...")
    l2distFromEarth_newt = newtonsMethod('l2')
  
    #format answers to something readable  
    l1distFromEarth_newt = '{:.3e}'.format(l1distFromEarth_newt - R)
    l2distFromEarth_newt = '{:.3e}'.format(l2distFromEarth_newt - R)
    print('\tL1 distance from Earth:', l1distFromEarth_newt, 'meters')
    print('\tL2 distance from Earth:', l2distFromEarth_newt, 'meters')


    #Secant method
    print('\n\n', 'SECANT METHOD:')
    print('\t', 'Calculating for L1...')
    l1distFromEarth_secant = secant('l1')
    print('\t', 'Calculating for L2...')
    l2distFromEarth_secant = secant('l2')

    #format answers to something readable  
    l2distFromEarth_secant = '{:.3e}'.format(l2distFromEarth_secant - R)
    l1distFromEarth_secant = '{:.3e}'.format(l1distFromEarth_secant - R)
    print('\tL1 distance from Earth:', l1distFromEarth_secant, 'meters')
    print('\tL2 distance from Earth:', l2distFromEarth_secant, 'meters')