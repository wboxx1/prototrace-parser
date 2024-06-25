# %%
import trace_pb2
import glob
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
%matplotlib notebook

# %% [markdown]
# # Introduction
# ## A bit of intruduction first.
# We use Google's protocol buffers for serializing our data.
# You can read about protocol buffers [here](https://developers.google.com/protocol-buffers).
# The [.proto](trace.proto) file defines our object attributes and is used by the protocol buffer compiler to create the [pb2.py](trace_pb2.py) file.
# The pb2.py file contains the class of functions we can use to store and parse the object we defined in the .proto file.

# %% [markdown]
# # Sample Data
# For the purpose of this demo, I will use a small sample of the data I sent you.
# The local samples are store in the [sample-data](sample-data/) folder.
# You will notice the data files are saved with a .ptc file extension.  This is a file extension we use to denote prototrace (protocol buffer trace) files.

# %%
# Set directories
input_directory = "sample-data/"

# Store file paths into list
input_files = glob.glob("{}{}".format(input_directory, "*.ptc"))

# %% [markdown]
# In order to parse the data, you need to create local trace object using the pb2.py file.
# I will only parse one file for this demo.

# %%
# Create trace object
trace = trace_pb2.Trace()

# Parse .ptc file
try:
    f = open(input_files[0], "rb")
    trace.ParseFromString(f.read())
    f.close()
except IOError:
    print(sys.arg[1] + ": Could not open file.")

# %% [markdown]
# Each .trc file has a list of attributes available.

# %%
# List of attributes
attributes = [
    "data",
    "scan_name",
    "start_frequency",
    "stop_frequency",
    "resolution_bandwidth",
    "video_bandwidth",
    "reference_level",
    "sweep_points",
    "auto_sweep_time",
    "sweep_time",
    "single_sweep_mode",
    "number_of_sweeps",
    "dwell_time",
    "coupling",
    "pre_amp_state",
    "attenuation",
    "auto_attenuation",
    "antenna_offset",
    "detector_type",
    "trace_type",
    "latitude",
    "longitude",
    "azimuth",
    "elevation",
    "measurement_date_time",
    "significant_digits",
]

# Attributs for the .trc file I parsed
for att in attributes:
    if att == "data":
        print("{}: [data array]".format(att, getattr(trace, att)))
    else:
        print("{}: {}".format(att, getattr(trace, att)))

# %% [markdown]
# The amplitude data is saved as integers in order to save space by taking advantage
# of the protocol buffer varint type. In order to convert back to doubles,
# the values are divided by 10^(trace.significant_digits)

# %%
data_y = np.array(trace.data) / (10 ** int(trace.significant_digits))

# %%
print("Data before conversion: {}".format(np.array(trace.data)[0:3]))
print("Data after conversion: {}".format(data_y[0:3]))

# %% [markdown]
# The frequency data is not stored as an array.
# The frequency array must be created using the start_frequency,
# stop_frequency, and sweep_points attributes

# %%
data_x = np.linspace(trace.start_frequency, trace.stop_frequency, trace.sweep_points)
# Sanity check
print("Start Frequency: {}".format(data_x[0]))
print("Stop Frequency: {}".format(data_x[-1]))
print("Amplitude data shape: {}".format(data_y.shape))
print("Frequency data shape: {}".format(data_x.shape))

# %% [markdown]
# A plot of the data represents the measured spectral data at that point in time.

# %%
def plot_trace(
    trace_x,
    trace_y,
    title="Trace Plot",
    xlabel="Frequency (MHz)",
    ylabel="Amplitude (dBuV/m)",
):
    plt.plot(trace_x, trace_y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ion()
    plt.show()


# %%
plot_trace(
    data_x, data_y, title="Trace Plot measured {}".format(trace.measurement_date_time)
)


# %%
