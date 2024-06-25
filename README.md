# Parser for protocol buffer 85EIS trace files.

This repo is set up to give instructions on how to parse the .ptc files in the data I sent you.  Each .ptc file represents a saved trace object created from spectrum analyzer data at a given time.  The trace object has 26 attributes.  Each attribute is defined below.

The following Binder link will take you to an interactive Jupyter Notebook which will guide you through an example of parsing the data.  The Binder may take some time to load.  If you don't want to or can't use the binder link, the notebook files are stored in this repo.  You can open them for reading on github or download them and run on your own Jupyter server for interactivity.

### Binder link for trace parser
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wboxx1/prototrace-parser.git/HEAD?labpath=trace_parse.ipynb)

The following Binder link will take you to a notebook which runs a replay of the dataset.  This shows the changes in the spectrum over time as we collected it.

### Binder link to replay notebook
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wboxx1/prototrace-parser.git/HEAD?labpath=replay_data.ipynb)

# Trace Attributes
What follows is descriptions of the trace attributes.

## trace.data
The data attribute holds the array of amplitude data points.  The size of this array is determined by the "sweep points" attribute.  This represents the raw data from the analyzer and so the units are normall in dBm.  The data is then later "replayed" and corrected using the appropriate losses and antenna factors.  I saved you this step and corrected the data into units of dBuV/m.  The data is saved as integers in order to save space by taking advantage of the protocol buffer varint type.  In order to convert the doubles into integers, the values were divided by 10^(**trace.significant_digits**).

## trace.significant_digits
This is an integer that represents the number of significant digits used when saving the data.  This value is needed to convert the data back to doubles.  To convert the data back from integers, multipy each value by 10^(**trace.significant_digits**).

## trace.scan_name
This is the name of the scan as set by our engineers.

## trace.start_frequency
This represents the frequency that corresponds to the first data point. Units are MHz.

## trace.stop_frequency
This represents the frequncy that correspons to the last data point.  The frequency for each data point can be inferred by using Start Frequency, Stop Frequency, and Sweep Points. Units are MHz.

## trace.resolution_bandwidth
This represents the resolution bandwidth setting of the analyzer at the time the data was collected.  Units are MHz.

## trace.video_bandwidth
This represents the video bandwidth setting of the analyzer at the time the data was collected.  Units are MHz

## trace.reference_level
This represents the reference level setting of the analyzer at the time the data was collected. Units are dBm.

## trace.sweep_points
This represents the sweep points setting of the analyzer at the time the data was collected.  This is directly responsible for the number of data points in the **trace.data** attribute.

## trace.auto_sweep_time
This is a boolean value that represents whether the sweep time was manually set (False) or was set by the analyzer (True).

## trace.sweep_time
This represents the time it takes for the analyzer to "sweep" the spectrum for this trace.  The units are ms.

## trace.single_sweep_mode
This is a boolean value used in our software to determine whether the number of sweeps will be explicitly set (True) or set by the analyzer (False).

## trace.number_of_sweeps
This represents the number of sweeps if **trace.single_sweep_mode** is set to True.

## trace.dwell_time
This represents the time the analyzer will sit at a trace and collect data.  This is only used if **trace.single_sweep_mode** is False.  The units are ms.

## trace.coupling
This represents the coupling setting of the analyzer.  It's either "ac" or "dc" on the analyzer but is represented by an enumeration integer in data: 0 represents "dc" and 1 represents "ac".
    
## trace.pre_amp_state
This is a boolean value that represents whether the internal pre-amp was on (True) or off (False) at the time of measurement.

## trace.attenuation
This value is used to tell the analyzer how much internal attenuation to use for this trace.  This value is only used if auto_attenuation is set to False.  Units are dB.

## trace.auto_attenuation
This is a boolean value that represents whether the amount of attenuation is set by the analyzer (True) or set by trace.attenuation (False).

## trace.antenna_offset
This represents the offset of the antenna from north.  When using a positioner, this represents the offset when the positioner is "home".  Units are degrees.

## trace.detector_type
This is an integer value that represents the detector setting of the analyzer used for this trace.  0 is peak, 1 is average, 2 is sample, 3 is normal, 4 is negative peak.

## trace.trace_type
This is an integer value that represents the type of trace used for this data set.  0 is clear write, 1 is max hold, 2 is min hold, 3 is trace average.

## trace.latitude
This represents the latitude of the measurement point.  I have set this to 0.  Units are normally decimal degrees.

## trace.longitude
This represents the longitude of the measurement point.  I have set this to 0.  Units are normally decimal degrees.

## trace.azimuth
This represents the azimuth of the positioner during this trace collection.  This is only useful if a positioner was used.  Units are degrees.

## trace.elevation
This represents the elevation above sea level during the measurement.  Units are meters.

## trace.measurement_data_time
This is the long data string representation of the date and time when the measurement was collected.
    



