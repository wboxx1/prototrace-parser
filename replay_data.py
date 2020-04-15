# %%
import sys
import glob
import trace_pb2
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set directories
# input_directory = sys.argv[1]
input_directory = "9ghz-to-18ghz-corrected/"

input_files = glob.glob("{}{}".format(input_directory, "*.ptc"))

fig, ax = plt.subplots(1, 1)

trace = trace_pb2.Trace()


def animate(ax):

    data_y = np.array(trace.data) / (10 ** int(trace.significant_digits))
    data_x = np.linspace(trace.start_frequency, trace.stop_frequency, len(data_y))

    if ax.lines:
        for line in ax.lines:
            line.set_xdata(data_x)
            line.set_ydata(data_y)

    ax.clear()
    ax.plot(data_x, data_y)
    # line1.set_ydata(data_y)
    # fig.canvas.draw()


for _file in input_files:
    try:
        f = open(_file, "rb")
        trace.ParseFromString(f.read())
        f.close()
        animate(ax)
    except IOError:
        print(_file + ": Could not open file.")


# %%
