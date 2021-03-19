import numpy as np
import matplotlib.pyplot as plt

def main():
    n = np.arange(151)
    x = 0.99*np.cos(n/10)
    # q2 = quantization(x, 2, max(x))
    # plt.plot(q2)
    # plt.show()

    # fig, ax = plt.subplots(3,1,constrained_layout=True)
    # fig.suptitle("Quantization")
    # ax[0].set_title("x[n]")
    # ax[0].stem(n,x, use_line_collection=True)
    q3 = quantization(x,3,1)  #3-bit quantization
    # ax[1].set_ylabel("Magnitude")
    # ax[1].set_title("3-bit quantization")
    # ax[1].stem(n, q3, use_line_collection=True)
    q8 = quantization(x,8,1)  #8-bit quantization
    # ax[2].set_xlabel("Samples (n)")
    # ax[2].set_title("8-bit quantization")
    # ax[2].stem(n, q8, use_line_collection=True)
    #QUANTIZATION 3-BIT
    plt.figure("Quan", constrained_layout=True)
    plt.title("3-bit Quantization")
    plt.stem(n,x, use_line_collection=True, markerfmt='bo',label="x[n]")
    plt.stem(n,q3, use_line_collection=True, markerfmt='go',label='x\u0302[n]')
    plt.xlabel("Samples (n)")
    plt.ylabel("Magnitude")
    #plt.stem(n,q8, use_line_collection=True, markerfmt='ro',label="8-bit")
    plt.legend()
    #ERROR
    fig, ax = plt.subplots(2,1,constrained_layout=True, sharex=True)
    fig.suptitle("Error")
    ax[0].set_title("3-bit")
    ax[0].stem(n,(q3-x), use_line_collection=True)
    ax[0].set_ylabel("Magnitude")
    #ax[0].stem(n,q3,use_line_collection=True)
    ax[1].set_title("8-bit")
    ax[1].stem(n,(q8-x), use_line_collection=True)
    ax[1].set_xlabel("Samples (n)")
    ax[1].set_ylabel("Magnitude")
    #ax[1].stem(n,q8,use_line_collection=True)

    B = [5,7,9,11,13,15]
    xp = np.logspace(-3,1,50)
    x = np.cos(n/10)*xp[:,np.newaxis]
    axis = np.sqrt(2)/xp
    fig, ax = plt.subplots()
    fig.suptitle("Signal to Noise Ratio")
    ax.set_xlabel("Samples (n)")
    ax.set_ylabel("Magnitude (dB)")
    for i in B:
        snr = np.zeros(len(xp))
        label = "B = {:d}".format(i)
        for j, xp_val in enumerate(xp):
            x = xp_val*np.cos(n/10)
            q = quantization(x,i,1)
            e = q - x
            snr[j] = compute_snrq(x,e)
        ax.semilogx(axis, snr, label=label)
        index_max = np.where(snr == max(snr))
        index_max = float(axis[index_max[0]])
        xpoint = "{:.2f}".format(index_max)
        ypoint = "{:.2f}".format(max(snr))
        point = '('+xpoint+','+ypoint+')'
        plt.annotate(s=point, xy=(index_max,max(snr)),
                     xytext=(index_max-1.5,max(snr)-2),
                     arrowprops=dict(facecolor='black'))
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1],labels[::-1])
    plt.show()

def quantization(x, B, X_m):
    step = X_m/(2**B)
    return np.clip(np.round(x/step)*step,-X_m,X_m-step)

def compute_snrq(x,e):
    return 10*np.log10(np.sum(x*x)/np.sum(e*e))

if __name__ == '__main__':
    main()
