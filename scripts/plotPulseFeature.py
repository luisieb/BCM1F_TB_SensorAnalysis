import sys
sys.path.append('../python')
import pandas as pd
import pandas as pd
from pylab import *
import seaborn as sns
from tb_DataReader import EventFeaturesReader
from tb_PulseAmpFitter import PulseAmpFitter

dataDir = "../data/eventFeatures"
run,backend="222","ubcm"
rd = EventFeaturesReader(dataDir,"000"+run,backend)
channel = 2
ch = rd.getChannel(channel)
sigma = ch.baseline_std.mean()


def plotFit():
  title = "Run {}, sensor-{} {}V, {} CH{}, n={}".format(run,2, 300,backend,channel,len(ch))
  # fitting
  fitter = PulseAmpFitter(ch.pulseAmp)
  fitter.fitRange(30,80,sigma)
  # plot
  fitter.plot()
  plt.title(title, fontsize=14)
  #plt.savefig("../plots/pulseAmpFit/langaus_{}_run{}_{}.png".format(backend,run,channel),dpi=300)


def plotHist2D():
  sns.set(style="ticks")
  jp= sns.jointplot(ch.pulseAmp, ch.pulsePos, kind="hex", color="C0",gridsize=20,ratio=4,space=0.5)
  jp.set_axis_labels(r'Amplitude','Position')
  #jp.ax_joint.plot([0,100])
  jp.ax_joint.set_title(title)
  #plt.savefig("../plots/PulseHist2D/{}_run{}_{}.png".format(backend,run,channel),dpi=300)

if __name__=="__main__":
  plotFit()
  plotHist2D()
  plt.show()
