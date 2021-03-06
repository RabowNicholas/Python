#Author: Nicholas Rabow
#Description: Extraction from h5 file type.
#             raw ECG signal typicals has 60 Hz interference.
#             This script removes that interference and cleans up the
#             preparing it to be interpreted.

import matplotlib.pyplot as plt
import numpy as np
import h5py

def main():
    #ECG data from h5 file
    f = h5py.File('ecg.h5')
    ecg = f.get('ecg')
    fs = f.get('fs')
    ecg = np.array(ecg)
    fs = np.array(fs)

    #Plot ecg with interference
    t = np.linspace(0,ecg.size/fs,ecg.size)
    plt.figure("INTERFERENCE")
    plt.plot(t,ecg)
    plt.xlim(9,10.2)
    plt.ylim(-1,1.5)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (mV)")
    plt.title("ECG Signal with 60 Hz Interference")

    w = np.linspace(-np.pi,np.pi,1000)
    h = [1,-2,1]
    # H = dtft(ecg,w)
    # fig, axs = plt.subplots(2, 1, sharex='all')
    # labels = ['-\u03C0',0, '\u03C0']
    # axs[0].set_title("Magnitude")
    # axs[1].set_title("Phase")
    # axs[1].set_xlabel("Frequency")
    # axs[1].set_ylabel("Radians")
    # axs[0].set_ylabel("Magnitude")
    # axs[0].plot(w,np.abs(H))
    # axs[1].plot(w,np.angle(H))
    # plt.xticks([-np.pi,0, np.pi],labels)

    #downsample the Signal
    #for minimum nyquist omega_n = 360 Hz
    #original sample rate of 3600/360 = M
    M = 10
    ecg_d = ecg[::M]
    #plt.plot(t[::M],ecg_d)

    #interference removal
    # w = np.linspace(-np.pi,np.pi,1000)
    # h = [1,-1,1]
    # H = dtft(h,w)
    # fig, axs = plt.subplots(2, 1, sharex='all')
    # labels = ['-\u03C0',0, '\u03C0']
    # axs[0].set_title("Magnitude")
    # axs[1].set_title("Phase")
    # axs[1].set_xlabel("Frequency")
    # axs[1].set_ylabel("Radians")
    # axs[0].set_ylabel("Magnitude")
    # axs[0].plot(w,np.abs(H))
    # axs[1].plot(w,np.angle(H))
    # plt.xticks([-np.pi,0, np.pi],labels)

    #discrete signal no noise
    y = myconv(ecg_d, h)
    # plt.figure("Conv")
    # plt.plot(t[::M], y[:len(t[::M])])
    # plt.xlim(9,10.2)
    # plt.ylim(-1,1.5)
    # plt.xlabel("Time (s)")
    # plt.ylabel("Voltage (mV)")
    # plt.title("Discrete ECG Signal without 60 Hz Interference")

    #cubic spline interpolation
    a = -0.5
    L = M
    hr = 1.0 * np.arange(2*M+1)
    hr[:L+1] = ((a+2)*(hr[:L+1]**3)/(L**3)
             -(a+3)*(hr[:L+1]**2)/(L**2)
             +1)
    hr[L+1:] = (a*(hr[L+1:2*L+1]**3)/(L**3)
                  -5*a*(hr[L+1:2*L+1]**2)/(L**2)
                  +8*a*hr[L+1:2*L+1]/L-4*a)
    hr = np.concatenate((np.flip(hr),hr[1:]))

    # H = dtft(hr, w)
    # fig, axs = plt.subplots(2, 1, sharex='all')
    # labels = ['-\u03C0',0, '\u03C0']
    # axs[0].set_title("Magnitude")
    # axs[1].set_title("Phase")
    # axs[1].set_xlabel("Frequency")
    # axs[1].set_ylabel("Radians")
    # axs[0].set_ylabel("Magnitude")
    # axs[0].plot(w,np.abs(H))
    # axs[1].plot(w,np.angle(H))
    # plt.xticks([-np.pi,0, np.pi],labels)
    yr = np.zeros(len(y)*M)
    yr[::M] = y
    yr = myconv(yr,hr)
    plt.figure("Recon")
    plt.plot(t, yr[:len(t)])
    plt.xlim(9,10.2)
    plt.ylim(-1,1.5)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (mV)")
    plt.title("Reconstructed ECG Signal without 60 Hz Interference")


    plt.show()
    f.close()

def dtft(x,w):
    X = np.zeros(len(w), dtype='complex')
    for k in range (len(x)):
        X += x[k]*np.exp(-1j*w*k)
    return X

def myconv(x, h):
    y = np.array(np.zeros(len(x)+len(h)-1))
    x = np.array(x)
    h = np.array(h)
    for i in range (len(x)):
        #print(i,y[i:len(h)+i], x[i]*h)
        y[i:len(h)+i] += x[i] * h
    return y

if __name__ == "__main__":
    main()
