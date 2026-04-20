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

# %%
# %load_ext autoreload 
# %autoreload 2

# %%
# with the code above, I can keep working in notebooks while I modify function in .py file

# %% [markdown]
# # Session6
# Today, we are going to learn packaging:
# * First we have to learn what is function in python
# * Make my own function 
# * Learn how to do python packaging configuration
# * Load the environment in notebook and use the package
#
# Note: This notebook is copied and modified from session4

# %% [markdown]
# ## Open the file
# Since we moved all the notebooks to another directory, I have to change data paths

# %%
# !pwd # check current working directory so that you can commit the path when opening a file

# %%
aFile = open ('/home/shch14/spaceMed2026/shch14/data/pulse_data.csv', 'r') # you can type the whole path

# %%
aFile = open ('../data/pulse_data.csv', 'r') # or just type ..


# %% [markdown]
# ## Function

# %%
def sum_prod (a,b,c=1):
    return c*(a+b)


# %%
sum_prod(1,2) #a=1, b=2

# %%
sum_prod(c=3,a=4,b=5) #you can change the order

# %%
sum_prod(c=3,4,5) #it should be error because we didn't assign variables a and b

# %%
name = "Mark"
age = "young"

# %%
print(name,age) #print is a sophisticated function which have different arguments

# %%
print(name, age, sep=" is ") # assign the seperater

# %%
print(name, age, sep=" is ", end=".") # assign the end


# %% [markdown]
# ## Exercise
# * move the data loader to a function called read_pulse
# * move the peak finding code to a function called
# find_peaks
# * move the heart rate calculation to a function called
# calc_heart_rate
# * and use those functions in the notebook

# %%
def read_pulse(file_name):
    aFile = open (file_name, 'r')
    aFile.readline()
    # read it so that we skip the firt line (or start the loop from second line)
    time = []
    absorption = []
    for line in aFile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    for i in range(10):
        print(time[i], absorption[i]) # I should return time and absorption!



# %%
read_pulse('../data/pulse_data.csv')


# %%
#answer
def readPulse(fname):
    dataFile = open (fname, 'r')
    dataFile.readline()
    time = []
    absorption = []
    for line in dataFile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
        
    return time, absorption


# %%
time, absorption = readPulse('../data/pulse_data.csv')


# %%
def findPeaks(time, absorption, w=50):
    w = w
    peaks = []
    for i in range(len(absorption)):
      start = max(i-w, 0)
      end = min(i+w, len(absorption))
      window = absorption[start:end]
      max_pos = numpy.argmax(window) + start
      if i == max_pos:
        peaks.append(i)
    return peaks


# %%
peaks = find_peaks(time, absorption)


# %%
def calc_heart_rate(time, peaks):
    time = numpy.array(time)
    time_peaks = time[peaks]
    delta_t = time_peaks[1:] - time_peaks[:-1]
    hr = 60 / delta_t
    return hr


# %%
hr = calc_heart_rate(time, peaks)

# %%
pyplot.plot(hr)
pyplot.show()

# %% [markdown]
# ## Use my spacemed fucntion!

# %%
import spacemed

# %%
spacemed.__version__

# %%
time, absorption = spacemed.readPulse('../data/pulse_data.csv')

# %%
Peaks = spacemed.findPeaks(time, absorption)

# %%
hr = spacemed.calHR(time, peaks)

# %%
pyplot.plot(hr)
