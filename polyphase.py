#Author: Nicholas Rabow
#Description: This script shows the increases in speed and
#             and decrease in computations of using polyphase
#             decompisition to decimate a signal. It is compared to
#             a naive implementation.

import numpy as np
import time
from scipy import signal
import matplotlib.pyplot as plt

def main():
#part A
    M = 4
    x = np.ones(64)
    x = np.pad(x, (32), 'constant')

    h = signal.firwin(16, 1/2/M)
    dtft(h,M)
    nd = naive_decimation(x,h,M)
    print(len(nd))
    pd = polyphase_decimation(x,h,M)
    print(len(pd))
    plt.figure("M=4")
    axis = np.arange(len(nd))
    plt.stem(axis,nd,use_line_collection=True,label='Naive',markerfmt='ro')
    plt.stem(axis,pd,use_line_collection=True,label='Polyphase')
    plt.legend()
    plt.xlabel("Samples (n)")
    plt.ylabel("Magnitude")
    plt.title("Polyphase vs. Naive Decimation (M=4)")
    plt.show()

#part B
    x = np.random.rand(2**16)
    M = [2,4,8,16,32,64]
    reps = 100
    for i in M:
        h = signal.firwin(128, 1/2/i)
        naive_time = 0
        poly_time = 0
        error = 0
        for j in range(reps):
            s = time.time()
            nd = naive_decimation(x,h,i)
            n = time.time()
            pd = polyphase_decimation(x,h,i)
            p = time.time()
            naive_time += (n-s)
            poly_time += (p-n)

            for k in range(int(len(nd)/4), int(3*len(pd)/4)):
                error += abs(nd[j]-pd[j])
        naive_time = naive_time / reps
        poly_time = poly_time / reps
        print("M={} Polyphase Time: {:.5f} Naive Time: {:.5f} Error: {:.3e}".format(
              i, poly_time, naive_time, error))


def naive_decimation(x,h,M):
    return myconv(x,h)[::M]

def polyphase_decimation(x,h,M):
    y = np.zeros(len(x)+len(h))[::M]
    x = np.concatenate((x,[0]))
    for i in range(M):
        y += myconv(np.concatenate((np.zeros(i),x))[::M],h[i::M])
    return y

def myconv(x,h):
    M = len(x)
    N = len(h)
    y = np.array(np.zeros(M+N-1))
    x = np.array(x)
    h = np.array(h)
    if M > N:
        for i in range(N):
            y[i:i+M] += x*h[i]
    else:
        for i in range (M):
            y[i:N+i] += x[i] * h
    return y

def dtft(x,M):
    w = np.linspace(-np.pi,np.pi,1000)
    X = np.zeros(len(w), dtype='complex')
    for k in range (len(x)):
        X += x[k]*np.exp(-1j*w*k)
    fig, axs = plt.subplots(2, 1, sharex='all')
    labels = ['-\u03C0','-\u03C0/2','-\u03C0/4',0,'\u03C0/4','\u03C0/2', '\u03C0']
    fig.suptitle("Anti-Aliasing Filter (M = {})".format(M))
    axs[0].set_title("Magnitude")
    axs[1].set_title("Phase")
    axs[1].set_xlabel("Frequency")
    axs[1].set_ylabel("Radians")
    axs[0].set_ylabel("Magnitude")
    axs[0].plot(w,np.abs(X))
    axs[1].plot(w,np.angle(X))
    plt.xticks([-np.pi,-np.pi/2,-np.pi/4,0,np.pi/4,np.pi/2, np.pi],labels)
    plt.show()

if __name__ == '__main__':
    main()
