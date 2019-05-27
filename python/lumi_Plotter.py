from pylab import *

def plotBunchCrossingHistogram(row, binsize=12):
    temp = row
    temp_histbx = temp.bx
    temp_n = temp_histbx.size
    temp_idxbx = np.arange(temp_n)

    plt.figure(figsize=(20,4),facecolor='w')
    plt.hist(temp_idxbx, np.arange(0,3564,binsize), weights = temp_histbx)
    plt.xlim(0,temp_n)
    plt.xlabel('index of bunch crossing')
    plt.title('Run-{:06d},    LumiSection-{:06d},    Nibble-{:06d}'.format(temp.runnum,temp.lsnum,temp.nbnum ))
    plt.grid(linestyle='--',alpha=0.5,color='0.5')
    plt.savefig('../plots/bxhist_run{}_ls{}_nb{}.png'.format(temp.runnum,temp.lsnum,temp.nbnum),dpi=200)