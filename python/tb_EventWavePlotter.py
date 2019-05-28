
from pylab import *
import pandas as pd

class EventWavePlotter():
    def __init__(self, dataDir,backend,loadNEvents=100):
        self.backend = backend
        self.loadNEvents = loadNEvents
        self.df = pd.read_csv(dataDir+"/{}.csv".format(backend), nrows=loadNEvents*4, header=None)
        self.waveLength = self.df.shape[1] - 2
        print("backend {}, wave lenth is {}".format(backend, self.waveLength) )

        
    def plotEvent(self, ievent):
        ev = self.df[self.df[0]=="EV{}".format(ievent)].reset_index(drop=True)
        plt.figure(facecolor="w",figsize=(10,8))
        for ich in range(4):
            plt.subplot(2,2,ich+1)
            #wave = ev[ev[1]=="CH{}".format(ich)].loc[:,2:]
            #print(wave)
            wave = ev.loc[ich,2:]
            plt.plot(wave)
            plt.title("{}, Event {}, CH {}".format(self.backend, ievent, ich))
            plt.xlim(0,self.waveLength)
            plt.ylim(80,260)
            plt.grid(linestyle='--',alpha=0.2,color='0.5')
        plt.savefig("../plots/event/{}_event{}".format(self.backend, ievent),dpi=200)
        
        
    def plotEvents(self):
        plt.figure(facecolor="w",figsize=(10,8))
        for ich in range(4):
            plt.subplot(2,2,ich+1)
            ch = self.df[self.df[1]=="CH{}".format(ich)].reset_index(drop=True)
            for i, row in ch.iterrows():
                wave = row[2:]
                plt.plot(wave,color='C0')
            plt.title("{}, CH {}, N={}".format(self.backend, ich,self.loadNEvents))
            plt.xlim(0,self.waveLength)
            plt.ylim(80,260)
            plt.grid(linestyle='--',alpha=0.2,color='0.5')
        plt.savefig("../plots/events/{}_N{}".format(self.backend,self.loadNEvents),dpi=200)
        
    def plotEventsHeatmap(self):
        x = np.arange(0,self.waveLength,1)
        
        ymin,ymax,ybinsize = 80,260,5
        ybin = np.arange(ymin,ymax+0.1,ybinsize)
        xbin = np.arange(0,self.waveLength+0.1,40)
        
        plt.figure(facecolor="w",figsize=(10,8))
        
        for ich in range(4):
            plt.subplot(2,2,ich+1)
            ch = self.df[self.df[1]=="CH{}".format(ich)].reset_index(drop=True)
            hist = []
            for i, row in ch.iterrows():
                wave = np.array(row[2:])
                temphist = np.histogram2d(x,wave,bins=(xbin,ybin))[0]
                hist.append(temphist)
            hist = np.sum(np.array(hist),axis=0)
            c = np.log(hist.T+0.01)
            plt.pcolor(xbin,ybin,c,linewidths=0,cmap='hot')
            plt.title("{}, CH {}, N={}".format(self.backend, ich,self.loadNEvents))
        plt.savefig("../plots/eventsHeatmap/{}_N{}".format(self.backend,self.loadNEvents),dpi=200)