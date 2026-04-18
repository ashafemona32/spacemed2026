# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-gpulab-2025-2]
#     language: python
#     name: conda-env-conda_envs-gpulab-2025-2-py
# ---

# %%
# import python library first
import numpy
from matplotlib import pyplot
import pandas
from scipy.signal import find_peaks

# %% [markdown]
# ---
# # Session5 - ECG with pandas and find_peaks

# %% [markdown]
# ## Find the Peaks

# %%
ecg = pandas.read_csv('data/pulse_data.csv')

# %%
ecg.head()

# %%
len(ecg['time'])

# %%
sampling_rate = 63065/180 # how many sample in 1 second
sampling_rate # 350Hz

# %%
#find the peaks
absorption = ecg['absorption']
time = ecg['time']
peaks,_ = find_peaks(absorption, height=2500, distance= 0.3 * 350) 
#,_ throw other piece of data into dummy variable
pyplot.plot(time, absorption, linewidth = 1.0)
pyplot.xlabel('Times(s)')
pyplot.ylabel('Absorption')
pyplot.title('Absorption with Peaks')
pyplot.plot(time[peaks], absorption[peaks], "rx")

# %% [markdown]
# ## HR calculation

# %%
#calculate the heart rate
time_peaks = times[peaks]
delta_t = time_peaks[1:] - time_peaks[:-1]
HR = 60 / delta_t
pyplot.plot(HR)
pyplot.ylabel('BPM')
pyplot.xlabel('Time(s)')
pyplot.title('Heart Rate')

# %% [markdown]
# ## 3-panel plot

# %%
#creat a big frame with three figures 3*1
frame, fig = pyplot.subplots(3, 1, figsize=(12, 12))
# the first one is raw signal
fig[0].plot(time, absorption, linewidth=1.0)
fig[0].set_title('1. Raw Absorption signal')
fig[0].set_xlabel('Time(s)')
fig[0].set_ylabel('Absorption')

# the second one is raw data with peaks
fig[1].plot(time, absorption, linewidth=1.0)
fig[1].plot(time[peaks], absorption[peaks], 'rx', markersize = 5)
fig[1].set_title('2. Absorption with Peaks')
fig[1].set_xlabel('Time(s)')
fig[1].set_ylabel('Absorption')

# the third one is HR
fig[2].plot(HR)
fig[2].set_title('3. Heart Rate')
fig[2].set_xlabel('Time(s)')
fig[2].set_ylabel('BPM')

pyplot.tight_layout()

# %% [markdown]
# ---
# # session4 - ECG with numpy

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Open the file

# %%
# !pwd # check current working directory so that yu can omit the path when openning a file

# %%
aFile = open ('data/pulse_data.csv', 'r')

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Extract data

# %%
# Read the data file
aFile.readline()
# read it so that we skip the firt line (or start the loop from second line)
time = []
absorption = []
for line in aFile.readlines():
    line = line.split(",")
    time.append(float(line[0]))
    absorption.append(float(line[1]))

# %%
print(len(time), len(absorption))

# %%
for i in range(10):
    print(time[i], absorption[i])

# %%
#pulse data I loaded earlier
pyplot.plot(time,absorption, linewidth = 1.0)
pyplot.ylabel('Absorption')
pyplot.xlabel('Time(s)')
pyplot.title('Pulse')
pyplot.show()

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Exercise - Find the peaks (session4)
# * Consider single cycle and come up with a naive solution
# * store all peak locations in a list or array
# * compute heart rate and plot it

# %%
w = 50
num_pnts = 1000

# %%
absorption = numpy.array(absorption)
time = numpy.array(time)
peaks = []

# %%
subset = absorption[:num_pnts]

# %%
for i in range(len(subset)):
    start = max(i-w, 0)
    end = min(i+w, len(subset))
    window = subset[start:end]
    max_pos = numpy.argmax(window) + start
    if i == max_pos:
        peaks.append(i)
print(peaks)


# %%
pyplot.plot(subset)
pyplot.xlabel("time [s]")
pyplot.ylabel("absorption")
pyplot.plot(peaks, subset[peaks], "ro")
pyplot.show()

# %%
peaks = []
for i in range(len(absorption)):
    start = max(i-w, 0)
    end = min(i+w, len(absorption))
    window = absorption[start:end]
    max_pos = numpy.argmax(window) + start
    if i == max_pos:
        peaks.append(i)
print(peaks)


# %%
pyplot.plot(absorption)
pyplot.xlabel("time[s]")
pyplot.ylabel("absorption")
pyplot.plot(peaks, absorption[peaks], "ro")
pyplot.show()

# %%
time_peaks = time[peaks]

# %%
delta_t = time_peaks[1:] - time_peaks[:-1]

# %%
hr = 60 / delta_t

# %%
pyplot.plot(hr)
