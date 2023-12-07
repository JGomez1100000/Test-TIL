import numpy as np

def multiply():
    d=0 # Number of tries
    while True: # Infinite loop until c==4
        a=np.random.randint(1,9)
        b=np.random.randint(1,9)
        c=a*b
        d+=1
        print(f'a:{a}, c:{c}, d:{d}')
        if c==4:
            print(f'Success! A: {a}, B: {b}')
            break


multiply()