#@author: Nicholas Rabow
#Description: Implementation of DTFT with example plots


from matplotlib import pyplot as plt
import numpy as np

def main():
    ##############
    ##RECT PULSE##
    ##############
    x = np.ones(5)
    w = np.linspace(-np.pi,np.pi,1000)
    X = dtft(x,w)
    labels = ['-\u03C0',0, '\u03C0']
    plt.figure("DTFT")
    plt.plot(w,np.abs(X))
    plt.title("DTFT of 5 point rectangle")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.xticks([-np.pi,0, np.pi],labels)

    plt.figure("Ref")
    X_ref = np.sin(2.5*w)/np.sin(w/2)
    plt.plot(w,X_ref)
    plt.title("Reference Sinc Function")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.xticks([-np.pi,0, np.pi],labels)

    fig, axs = plt.subplots(2, 1, sharex='all')
    axs[0].set_title("Real Values")
    axs[1].set_title("Imaginary Values")
    axs[1].set_xlabel("Frequency")
    axs[1].set_ylabel("Magnitude")
    axs[0].set_ylabel("Magnitude")
    axs[0].plot(w,np.real(X))
    axs[1].plot(w,np.imag(X))
    plt.xticks([-np.pi,0, np.pi],labels)

    plt.show()

    ############
    ##EXP FUNC##
    ############
    L = 500
    n = np.arange(L)
    x = 0.9**n
    plt.figure("OG")
    plt.title("Exponential Decay Discrete Function")
    plt.xlabel("Samples (n)")
    plt.ylabel("Magnitude")
    plt.stem(n,x, use_line_collection = 'true')

    w = np.linspace(-np.pi,np.pi,L)
    X = dtft(x,w)
    labels = ['-\u03C0',0, '\u03C0']
    plt.figure("DTFT")
    plt.plot(w,np.abs(X))
    plt.title("DTFT of decaying exponential")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.xticks([-np.pi,0, np.pi],labels)

    plt.figure("Ref")
    X_ref = 1/(1-0.9*np.exp(-1j*w))
    plt.plot(w,np.real(X))
    plt.title("Reference Function")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.xticks([-np.pi,0, np.pi],labels)

    fig, axs = plt.subplots(2, 1, sharex='all')
    axs[0].set_title("Real Values")
    axs[1].set_title("Imaginary Values")
    axs[1].set_xlabel("Frequency")
    axs[1].set_ylabel("Magnitude")
    axs[0].set_ylabel("Magnitude")
    axs[0].plot(w,np.real(X))
    axs[1].plot(w,np.imag(X))
    plt.xticks([-np.pi,0, np.pi],labels)
    plt.show()

    plt.show()

def dtft(x,w):
    X = np.zeros(len(w),dtype='complex')
    for k in range (len(x)):
        X += x[k]*np.exp(-1j*w*k)
    return X

if __name__ == "__main__":
    main()
