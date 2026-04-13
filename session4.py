# ---
# title: "Session 4: Reproducible Documents"
# author: Magnus Hagdorn
# format:
#   html:
#     code-fold: true
#   pdf:
#     echo: false
#     pdf-engine: pdflatex
#     toc: true
#     number-depth: 2
#     number-sections: true
#     papersize: a4
#     documentclass: article
# jupyter: python3
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

# %% [markdown]
# # Session4
# Today, we are going to learn how to design algorithm, including:
# * What is Reproducible Documents and how to create/publish them with quarto
# * 
# * 
# Note: This notebook is copied and modified from session3

# %% [markdown]
# # Rocket Equation
# At time $t_0$ to rocket starts to expel gas at a
# constant mass flow rate $R$ meassured in kg/s
# and exhaust velocity relative to the rocket 
# $v_e$ in m/s.
# $$
# \frac{dv}{dt} = -\frac{F}{m(t)} = -\frac{Rv_e}{m(t)}
# $$ {#eq-rocket-acc}
# Integrating both sides of @eq-rocket-acc from 0
# to $T$ we get

# %% [markdown]
# ## Open the file

# %%
# !pwd # check current working directory so that yu can omit the path when openning a file

# %%
aFile = open ('data/pulse_data.csv', 'r')

# %% [markdown]
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
# import python library first
import numpy
from matplotlib import pyplot

# %%
#| label: fig-dataset
#| fig-cap: "Measurements from an oxymetry sensor as a
#| function of time for 3 cycles"
#pulse data I loaded earlier
pyplot.plot(time,absorption, linewidth = 1.0)
pyplot.ylabel('Absorption')
pyplot.xlabel('Time(s)')
pyplot.title('Pulse')
pyplot.show()

# %% [markdown]
# # Array

# %%
a = numpy.array([1,2,3,4,5])
print(a)

# %%
a.shape

# %%
a.dtype

# %%
a.nbytes

# %%
a = numpy.array([1,2,3,4,5],dtype=float)
print(a)

# %%
b = numpy.array([[1,2],[3,4]])
print(b)

# %%
c = numpy.zeros([10,20])
print(c)
c.shape

# %%
d = numpy.arange(0,10)+1
print(d)
d.shape

# %%
d.dtype

# %%
d.nbytes

# %%
d.T @ d #'@'means vector product 

# %%
e = numpy.logspace(1,10,10)
print(e)
e.shape

# %%
e = numpy.array([[1,2,3], [4,5,6]])

# %%
e.shape

# %%
e.T * 2

# %%
e.T @ e 

# %%
d = numpy.linspace(0,10,21)
print(d)
d.shape

# %%
a

# %%
numpy.max(a)

# %%
numpy.argmax(a) # where maximum occurs

# %% [markdown]
# ### Exercise - Find the peaks
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

# %%
peaks = []
for i in len(absorption):
    if i+1 - i < 0:
        p = absorption[i]
        p_pos = i
        peaks.append(absorption[i])
        
