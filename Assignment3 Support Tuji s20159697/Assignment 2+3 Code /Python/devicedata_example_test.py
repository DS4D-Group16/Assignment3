"""
@author JK

This script uses Niklas Berliner's data interface module to read in
some room data for a home, and then displays it as a graph, indexed by
the room type

Usage: python devicedata_example.py --homeid=90 --measure='humidity' --samplerate=1000
"""
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IdealDataInterface import IdealDataInterface

# Set up arguments to be parsed and their default values
parser = argparse.ArgumentParser(description='Display some IDEAL room data from CSV files')
parser.add_argument('--homeid',type=int, default=1868, help='home to process, default 1868')
parser.add_argument('--inputdir', type=str, default='./SMILE/', help='directory where source files are')
parser.add_argument('--samplerate', type=str, default="300", help='sample rate in seconds')
args = parser.parse_args()

# initialize the data interface
idi = IdealDataInterface(args.inputdir)

# grab all appliance use readings for a home
readings = idi.get(homeid=args.homeid,category='electric-appliance')

# display the data on a graph
rlist=[]
legend=[]
for res in readings:
    # downsample the data to the specified granuarity - best to do
    # this before plotting forward fill is normally valid because IAMs
    # record change in power rather than regular readings; however
    # there are cases where the return to zero state is missing, so
    # care should be taken..
    rlist.append(res['readings'].resample(args.samplerate+"s").mean().ffill())
    legend.append(res['subtype'])
    
combo=pd.concat(rlist, axis=1)
plt.figure()
plt.plot(combo)
plt.legend(legend)
plt.title("Home "+str(args.homeid)+": device usage ")
plt.xlabel("Date / time")
plt.ylabel("Watts")
plt.show()

