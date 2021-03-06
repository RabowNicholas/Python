#Author: Nicholas Rabow
#Description: Convolution function with only one for loop

import numpy as np

def main():
    x = [1,2,3,4,5]
    h = [6,7,8,9]
    print(np.convolve(x,h))
    print(myconv(x,h))
    x = np.random.random(1000)
    h = np.arange(168)
    print(np.convolve(x,h))
    print(myconv(x,h))
def myconv(x,h):
    y = np.array(np.zeros(len(x)+len(h)-1))
    x = np.array(x)
    h = np.array(h)
    for i in range (len(x)):
        y[i:len(h)+i] += x[i] * h
    return y
if __name__ == "__main__":
    main()
