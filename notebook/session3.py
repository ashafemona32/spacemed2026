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
# # Session3
# Today, we are going to learn how to read data, including:
# * How to open/ read/ write the file
# * How to extract data for analysis
# * How to draw a plot for the data

# %% [markdown]
# ## Open the file

# %%
# !pwd # check current working directory so that you can omit the path when openning a file

# %%
aFile = open ('../data/pulse_data.csv', 'r')

# %% [markdown]
# ## Extract your data

# %% [markdown]
# #### Exercie 
# * open the file data/pulse_data.csv
# * you will need to ignore the first line (bcs it's just header)
# * read the two columns into two lists
# * convert the data to floats

# %%
# My trying
firstCol = []
secondCol = []
for line in aFile.readlines()[1:]:
    firstCol.append(float(line.split(",")[0]))
    secondCol.append(float(line.split(",")[1]))

aFile.close()
print(firstCol[:5])
print(secondCol[:5])
print (len(firstCol), len(secondCol))

# %%
# Answer
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
print(time[0:10])
print(absorption[0:10])

# %%
for i in range(10):
    print(time[i], absorption[i])

# %% [markdown]
# ### Relection about my solution:
# * use header as list name instead of general description
#    (time&absorption vs firstCol&secondCol)
# * you can use readline instead of index for skip the first line
# * print list in more organized way!

# %% [markdown]
# ## Visualize your data

# %%
# import python library first
import numpy
from matplotlib import pyplot

# %%
# generate 500 random samples from a standard normal distribution
x=numpy.random.normal(size=(500,))
y=numpy.random.normal(size=(500,))

# %%
pyplot.plot(x,y) #plot them

# %%
pyplot.plot(x,y, "oy") # change markers "o" and color "y"

# %%
pyplot.plot(x,y, "oy") # change markers "o" and color "y"
pyplot.xlabel("x") # add label
pyplot.ylabel("y")

# %%
pyplot.plot(x,y, "oy") # # change markers "o" and color "y"
pyplot.xlabel("x") # add label
pyplot.ylabel("y")
pyplot.title("Here is the title") # add title

# %%
#pulse data I loaded earlier
pyplot.plot(time,absorption, linewidth = 1.0)
pyplot.ylabel('Absorption')
pyplot.xlabel('Time')
pyplot.title('Pulse')
pyplot.show()

# %%
