import pandas as pd
from pylab import *

class EventFeaturesReader():
  def __init__(self, dataDir, run, backend):
    self.dataDir = dataDir
    self.run = run
    self.backend = backend

    fileName = dataDir+"/{}_run{}".format(backend,run)
    self.data = pd.read_csv(fileName+"_eventFeatures.csv")
    self.data["pulseAmp_sigmaNoise"] = self.data.pulseAmp/self.data.baseline_std

  def getChannel(self,channel):
    ch = self.data.query("ch=={}".format(channel))
    
    if self.backend == "VME": #Added cut on pulseAmp_simaNoise 
      ch = ch.query(" pulsePos<{} & pulsePos>{} & pulseAmp_sigmaNoise>{}".format(1415+10,1415-10,5))
    if self.backend == "ubcm":
      ch = ch.query(" pulsePos<{} & pulsePos>{} & pulseAmp_sigmaNoise>{}".format(295+25,295-20,5))

    ch.reset_index(drop=True, inplace=True)
    return ch


