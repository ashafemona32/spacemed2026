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
#     display_name: Python [conda env:.conda-spacemed26]
#     language: python
#     name: conda-env-.conda-spacemed26-py
# ---

# %% [markdown]
# # Session8
# Today we are going to learn how to analysis multi-dimensional data by analyzing fMRI dataset with `nibabel` and `seaborn`

# %% [markdown]
# ## fMRI Data
# we can check MRI data (images) just using python!

# %%
from matplotlib import pyplot
import nibabel
import pandas
import seaborn
import numpy
import scipy.signal

# %%
pwd

# %% [markdown]
# ### Just MRI data for building anatomy

# %%
anatomy = nibabel.load("../fmri-data/2_Anatomy_1mm_5min.nii")

# %%
print(anatomy.header) #quickly check the dataset

# %%
print(anatomy.shape) #it will show the dataset is 3D and how many slices we have

# %%
print(anatomy.header.get_zooms())

# %%
data_anatomy = anatomy.get_fdata() # extract data

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(data_anatomy[120, :, :].T, # .T means transportation 
    origin="lower", # origin tells the vertical orientation
    cmap="gray")

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(data_anatomy[96, :, :].T, # change to different slice
    origin="lower", 
    cmap="gray")

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(data_anatomy[:, 120, :].T, 
    origin="lower",
    cmap="gray")

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(data_anatomy[:, :, 120].T, 
    origin="lower",
    cmap="gray")

# %% [markdown]
# If we have different datasets then we have to map them together.
# In this condition, we use `.affine` to do the transformation  (rotate and translate)

# %%
print(anatomy.affine) # I have dataset called anatomy
# another dataset called fmri: print(fmri.affine)

# %% [markdown]
# ## Run correlation

# %% [markdown]
# We have to learn how to run correlation in python first

# %%
ols = pandas.read_csv("../data/ols.csv")

# %%
ols

# %%
# run correlation
seaborn.regplot(
    ols,
    x='Initial Mass (kg)',
    y='Payload Mass to LEO (kg)',
    order=1)

# %%
seaborn.regplot(
    ols,
    x='Length (m)',
    y='Payload Mass to LEO (kg)',
    order=1)

# %%
seaborn.regplot(
    ols,
    x='Length (m)',
    y='Payload Mass to LEO (kg)',
    order=2) # change the order to make the prediction fit the data  

# %% [markdown]
# **Now go back to fMRI Data!**

# %%
fmri = nibabel.load("../fmri-data/3_fMRI_TR2sec_3mm_3min.nii")

# %%
fmri.shape

# %%
print(fmri.header.get_zooms())

# %%
nt = fmri.shape[-1]

# %%
sampling_rate = fmri.header.get_zooms()[-1]

# %%
print(nt, sampling_rate)

# %%
p1 = (19,24,25) # assign what I want to extract
p2 = (40,25,25)
p3 = (19,25,25)

# %%
fmri_data = fmri.get_fdata() # get data from the dataset

# %%
fmri_data[p1]

# %%
pyplot.plot(fmri_data[p1])
pyplot.plot(fmri_data[p2])
pyplot.plot(fmri_data[p3])

# %%
# since the sampling rate is 2 seconds, and the setting is 10s on and 10s off
# we need 5 datapoints for each condition
s_one = numpy.array([1]*5 + [0]*5)

# %%
s_one

# %%
#use tile we can pile up our array based on the times we assign 
numpy.tile(s_one,2) # 2 means we want 20-second block

# %%
# since we use 10s as unit, we repeated ceiling of nt/10 to cover all the datapoints
signal = numpy.tile(s_one, int(numpy.ceil(nt/10)))

# %%
signal = signal[:nt]

# %%
pyplot.plot(signal)


# %%
# make a function for normalizing data
def normalise(data):
    norm = (data - numpy.mean(data))
    norm = norm / numpy.std(data)
    return norm


# %%
pyplot.plot(normalise(fmri_data[p1]))
pyplot.plot(normalise(fmri_data[p2])) # the orange one is like noise
pyplot.plot(normalise(fmri_data[p3]))

# %%
freq, power = scipy.signal.periodogram(normalise(fmri_data[p1]),
                                      fs=1/sampling_rate)
#freqency consent with time series to show the distribution
#it's a kind of FFT

# %%
pyplot.plot(freq,power)

# %%
# now let's run each frequency with loop
for p in (p1, p2, p3):
    freq, power = scipy.signal.periodogram(normalise(fmri_data[p]),
                                      fs=1/sampling_rate)
    pyplot.plot(freq,power)

# %%
# right now try to overlap the signal together -- cross correlation
# do p1 first
data = fmri_data[p1]
cross = scipy.signal.correlate(
    normalise(data), normalise(signal),
    mode="same")
lags = scipy.signal.correlation_lags(
    len(data), len(signal),
    mode="same")

# %%
p = numpy.argmax(cross)

# %%
lags[p] # peaks is at 8 seconds (something happened here)

# %%
pyplot.plot(lags, cross)

# %%
# let's run for loop again
for p in (p1,p2,p3):
    data = fmri_data[p]
    cross = scipy.signal.correlate(
        normalise(data), normalise(signal),
        mode="same")
    lags = scipy.signal.correlation_lags(
        len(data), len(signal),
        mode="same")
    pyplot.plot(lags, cross)

# we can successfully filter out noise now

# %%
corr_map = numpy.zeros(fmri.shape[:2]) #create 2D array

# %%
z = 25 #z as slice index

# %%
#align with time series 
for x in range(corr_map.shape[0]):
    for y in range(corr_map.shape[1]):
        time_series = fmri_data[x,y,z, :]
        cross = scipy.signal.correlate(
            normalise(time_series), 
            normalise(signal), 
            mode="same")
        corr_map[x,y] = numpy.max(cross)


# %%
fig, axes = pyplot.subplots(1)
image_plot = axes.imshow(corr_map.T,
                        origin="lower",
                        cmap="grey")

# %%
# with filter
background_threshold = 250
for x in range(corr_map.shape[0]):
    for y in range(corr_map.shape[1]):
        time_series = fmri_data[x,y,z, :]
        if numpy.mean(time_series) < background_threshold: 
            corr_map[x, y] = 0
            continue
        cross = scipy.signal.correlate(
            normalise(time_series), 
            normalise(signal), 
            mode="same")
        corr_map[x,y] = numpy.max(cross)

# %%
brain = numpy.mean(fmri_data[:,:,z,:], axis = -1)

# %%
overlap_map = numpy.copy(corr_map)

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(brain.T,origin="lower",cmap="grey")
axes.imshow(overlap_map.T,origin="lower",cmap="viridis", alpha = 0.5) 
#overlap fMRI to the 'brain' with adapting transperancy

# %% [markdown]
# ## Checking my spacemed function

# %%
import spacemed
corr_map1 = numpy.zeros(fmri.shape[:2])

# %%
background_threshold = 250
for x in range(corr_map.shape[0]):
    for y in range(corr_map.shape[1]):
        time_series = fmri_data[x,y,z, :]
        if numpy.mean(time_series) < background_threshold: 
            corr_map1[x, y] = 0
            continue
        cross,lag,p = spacemed.fmriCross(signal, fmri_data, (x,y,z))
        corr_map1[x,y] = numpy.max(cross)

# %%
print(lag, p)

# %%
brain = numpy.mean(fmri_data[:,:,z,:], axis = -1)
overlap_map = numpy.copy(corr_map1)
    
fig, axes = pyplot.subplots(1)
axes.imshow(brain.T,origin="lower",cmap="grey")
axes.imshow(overlap_map.T,origin="lower",cmap="viridis", alpha = 0.5) 

# %%
