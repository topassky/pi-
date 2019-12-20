import numpy as np

def pi():
    
    contador=0
    for i in range (0, 100000):
        x = np.random.rand()
        y = np.random.rand()
        if (x**2+y**2 <= 1 ):
            contador+=1
    pi = 4*(contador/100000.0)
    
    print(pi)
    

pi()
