import matplotlib.pyplot as plt
import numpy as np
import sys
import getopt


class WD:
  def __init__(self,experiment,fs,nlayer,filename):
    self.experiment = experiment
    self.fs = fs
    self.nlayer = nlayer
    self.filename = filename

  def loadWeightFile(self):
    p = "../results/exp{}/{}".format(self.experiment,self.filename)
    d = np.loadtxt(p)
    return d


# check if we run this as a main program
if __name__ == "__main__":
  experiment = 1
  fs = 48000
  nlayer = 5
  weight_filename = "weight_distance.tsv"
  save_file = False

  helptext = 'usage: {} -p experiment -l nlayer -f file -s -h'.format(sys.argv[0])
  
  try:
    # Gather the arguments
    all_args = sys.argv[1:]
    opts, arg = getopt.getopt(all_args, 'p:l:f:s')
    # Iterate over the options and values
    for opt, arg_val in opts:
      if '-p' in opt:
        experiment = int(arg_val)
      elif '-l' in opt:
        nlayer = int(arg_val)
      elif '-f' in opt:
        weight_filename = arg_val
      elif '-s' in opt:
        save_file = True
      elif '-h' in opt:
        raise getopt.GetoptError()
      else:
        raise getopt.GetoptError()
  except getopt.GetoptError:
    print (helptext)
    sys.exit(2)

  plt.figure("Weight Development",figsize=(16,12),dpi=80)
  wd = WD(experiment,fs,nlayer,weight_filename)
  
  d = wd.loadWeightFile()
  x = np.arange(0.0,160.0,160/d.shape[0])
  plt.plot(x,d[:,0],label="d_all")

  for layer in range(nlayer):
    plt.plot(x,d[:,layer+1],label="d_{}".format(layer))
  
  plt.ylabel("weight distance")
  plt.xlabel("t/sec")
  plt.legend()
  
  if save_file:
    plt.savefig("../results/exp{}/weightDevelopment.png".format(experiment))
  else:
    plt.show()
