#!/usr/bin/env python

import pandas as pd
from tb_EventWavePlotter import *

if __name__=="__main__":
  dataDir = "../data/eventWaves"
  pt = EventWavePlotter(dataDir,"ubcm",loadNEvents=100)
  pt.plotEventsHeatmap()
  pt.plotEvent(9)
  #pt.plotEvents()
  plt.show()