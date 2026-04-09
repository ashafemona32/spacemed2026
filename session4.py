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

# %% [markdown]
# # Session4
# Today, we are going to learn how to design algorithm, including:
# * 
# * 
# * 
# Note: This notebook is copied from session3

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
#pulse data I loaded earlier
pyplot.plot(time,absorption, linewidth = 1.0)
pyplot.ylabel('Absorption')
pyplot.xlabel('Time(s)')
pyplot.title('Pulse')
pyplot.show()

# %%
