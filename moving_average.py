#@author: Nicholas Rabow
#description: This script shows the effect that a moving average hows on noise/interference

import numpy as np
import matplotlib.pyplot as plt

def main():
    #Exponential Signal with error added that is corrected by adding 5 point MA filter
    #s[n] signal
    n = np.arange(0,101)
    s_n = 2*n * 0.9**n
    #gaussian random noise
    mu, sigma = 0, 1
    w_n = np.random.normal(mu,sigma,101)
    x_n = s_n + w_n

    plt.figure("MA w/ noise")
    plt.xlabel("Samples(n)")
    plt.ylabel("Magnitude")
    plt.title("Moving Average effect on Noise")
    plt.stem(n, s_n, label="Reference",linefmt=':', markerfmt='bo', use_line_collection='true')
    plt.stem(n, x_n, label="Gaussian Error",linefmt=':', markerfmt='go', use_line_collection='true')
    y_n5 = MA(x_n,5)
    plt.stem(n, y_n5, label="5 Point Moving Average",linefmt=':', markerfmt='ro', use_line_collection='true')

    plt.legend(loc='upper right')
    plt.show()
    
    
    #Same as above except instead of noise, there will be an interfering signal
    n_int = np.arange(0,51)
    w_int = np.cos(np.pi*0.4*n_int)
    w_int = np.pad(w_int, (0,50), 'constant')
    x_int = s_n + w_int
    
    plt.figure("MA w/ inteference")
    plt.xlabel("Samples(n)")
    plt.ylabel("Magnitude")
    plt.title("Moving Average effect on inteference")
    plt.stem(n, s_n, label="Reference",linefmt=':', markerfmt='bo', use_line_collection='true')
    plt.stem(n, x_int, label="Interference",linefmt=':', markerfmt='go', use_line_collection='true')
    x_int4 = MA(x_int, 4)
    plt.stem(n, x_int4, label="4 Point Moving Average",linefmt=':', markerfmt='yo', use_line_collection='true')
    x_int5 = MA(x_int, 5)
    plt.stem(n, x_int5, label="5 Point Moving Average",linefmt=':', markerfmt='mo', use_line_collection='true')
    x_int6 = MA(x_int, 6)
    plt.stem(n, x_int6, label="6 Point Moving Average",linefmt=':', markerfmt='ro', use_line_collection='true')
    plt.legend(loc='upper right')
    plt.show()
    
def MA(x,window):
    w = window
    m = np.ones(w)/w
    y = np.convolve(x,m,'same')
    return y
if __name__ == "__main__":
   main()
   