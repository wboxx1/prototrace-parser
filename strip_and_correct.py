import sys
import glob
import trace_pb2
import pandas as pd
import numpy as np
from scipy import interpolate
from os import listdir, path

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


# define a data scaling function
def scale_data(data, antenna_factors, losses):
    # dBm to dB/m
    scaled_data = np.fromiter(
        (x + y for x, y in zip(data, antenna_factors)),
        "float64"
    )

    # dBm/m to dBuV/m
    scaled_data = np.add(scaled_data, 107)

    # Add in losses
    scaled_data = np.fromiter(
        (x - y for x, y in zip(scaled_data, losses)),
        "float64"
    )

    return scaled_data


# Set directories
print(sys.argv)
input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Get file names for cal data
antenna_file = glob.glob(input_directory + "*.ant")[0]
# antenna_file = [f for f in listdir(input_directory) if file.endswith(".ant")]
cal_file = glob.glob(input_directory + "*.csv")[0]
print(antenna_file)
print(cal_file)

# Extract calibration data
antenna = pd.read_csv(antenna_file, header=1)
rows_to_skip = [*range(18), 10019]
losses = pd.read_csv(
    cal_file,
    skiprows=lambda x: x in rows_to_skip,
    names=["Hz", "Loss"],
    dtype="float64"
)

# Extract antenna data into arrays
ant_x = np.array(antenna["! MHz"])
ant_y_db = np.array(antenna["Gain(dB)"])
ant_y_af = np.array(antenna["AF"])

# Extract losses into arrays
loss_x = np.array(losses["Hz"])
loss_y = np.array(losses["Loss"])

# Convert Hz to MHz
loss_x = np.divide(loss_x, 1e6)

input_files = glob.glob("{}{}".format(input_directory, "*.ptc"))

for _file in input_files:
    trace = trace_pb2.Trace()
    try:
        f = open(_file, "rb")
        trace.ParseFromString(f.read())
        f.close()
    except IOError:
        print(_file + ": Could not open file.")

    data_y = np.array(trace.data) / (10**int(trace.significant_digits))
    data_x = np.linspace(
        trace.start_frequency,
        trace.stop_frequency,
        len(data_y)
    )

    # create interpolators for the antenna and loss arrays to fit the data
    interpolator_db = interpolate.interp1d(ant_x, ant_y_db)
    interpolator_af = interpolate.interp1d(ant_x, ant_y_af)
    interpolator_loss = interpolate.interp1d(loss_x, loss_y)

    # apply the interpolators to the data
    interpd_ant_data_db = interpolator_db(data_x)
    interpd_ant_data_af = interpolator_af(data_x)
    interpd_losses = interpolator_loss(data_x)

    # Scale the data
    scaled_data = scale_data(data_y, interpd_ant_data_af, interpd_losses)

    # convert scaled data to integers
    integer_scaled_data = (scaled_data * 10**int(trace.significant_digits)).astype("int")

    # Set new trace data to new data
    trace.data[:] = integer_scaled_data
    # for datum in integer_scaled_data:
    #     trace.data.add(datum)

    # Clear Lat, Lon
    trace.latitude = 0
    trace.longitude = 0

    # Save new trace file
    new_location = output_directory + path.split(_file)[-1]
    f = open(new_location, "wb")
    f.write(trace.SerializeToString())
    f.close()
