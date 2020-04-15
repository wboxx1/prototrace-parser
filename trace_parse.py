# %%
import trace_pb2
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# %%
attributes = [
    # data,
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

# %%
trace = trace_pb2.Trace()
try:
    f = open("trace.ptc", "rb")
    trace.ParseFromString(f.read())
    f.close()
except IOError:
    print(sys.arg[1] + ": Could not open file.")

# %%
for att in attributes:
    print("{}: {}".format(att, getattr(trace, att)))

# %%
data_y = np.array(trace.data) / (10 ** int(trace.significant_digits))

# %%
print(data_y[0:3])

# %%
data_x = np.linspace(trace.start_frequency, trace.stop_frequency, len(data_y))

# %%
print(data_x[0])
print(data_x[-1])
print(data_x.shape)
# %%
antenna = pd.read_csv("Qpar218.ant", header=1)
rows_to_skip = [*range(18), 10019]
losses = pd.read_csv(
    "2G_to_9G.csv",
    skiprows=lambda x: x in rows_to_skip,
    names=["Hz", "Loss"],
    dtype="float64",
)
print(antenna.head())
print(losses.head())
print(losses.tail())

# %%
# Extract antenna data into arrays
ant_x = np.array(antenna["! MHz"])
ant_y_db = np.array(antenna["Gain(dB)"])
ant_y_af = np.array(antenna["AF"])

# %%
# Extract losses into arrays
loss_x = np.array(losses["Hz"])
loss_y = np.array(losses["Loss"])

# %%
# Convert Hz to MHz
loss_x = np.divide(loss_x, 1e6)

# %%
# create interpolators for the antenna and loss arrays to fit the data
interpolator_db = interpolate.interp1d(ant_x, ant_y_db)
interpolator_af = interpolate.interp1d(ant_x, ant_y_af)
interpolator_loss = interpolate.interp1d(loss_x, loss_y)

# %%
# apply the interpolators to the data
interpd_ant_data_db = interpolator_db(data_x)
interpd_ant_data_af = interpolator_af(data_x)
interpd_losses = interpolator_loss(data_x)

# %%
# Sanity check
print("Data shape: {}".format(data_y.shape))
# print("Ant data shape: {}".format(interpd_ant_data_db.shape))
print("Ant data shape: {}".format(interpd_ant_data_af.shape))
print("Cal data shape: {}".format(interpd_losses.shape))


# %%
# define a data scaling function
def scale_data(data, antenna_factors, losses):
    # dBm to dB/m
    scaled_data = np.fromiter((x + y for x, y in zip(data, antenna_factors)), "float64")

    # dBm/m to dBuV/m
    scaled_data = np.add(scaled_data, 107)

    # Add in losses
    scaled_data = np.fromiter((x - y for x, y in zip(scaled_data, losses)), "float64")

    return scaled_data


# %%
# Scale the data
scaled_data = scale_data(data_y, interpd_ant_data_af, interpd_losses)


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
plot_trace(data_x, data_y, title="uncorrected", ylabel="Amplitude (dBm)")
plot_trace(data_x, scaled_data, title="corrected")

# %%
