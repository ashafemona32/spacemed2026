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
# ## Use my spacemed function for Pulse Data Analysis!
# Here I used the `spacemed` package (containing functions built in Session 4) to process raw pulse signal data and visualize heart rate over time.

# %% [markdown]
# **First step:** Imports the `spacemed` and uses `readPulse` to read absorption data.

# %%
import spacemed

# %%
spacemed.__version__ # check version of my package

# %%
time, absorption = spacemed.readPulse('../data/pulse_data.csv') #.. means previous directory

# %% [markdown]
# **Second step:** Uses `findPeaks` function to identify signal peaks within the pulse data.

# %%
peaks = spacemed.findPeaks(time, absorption) # window(w) is default vaulue (50)

# %% [markdown]
# **Third step:** Uses `calR` function to compute the heart rate (BPM) based on the timing of detected peaks.

# %%
hr = spacemed.calHR(time, peaks)

# %% [markdown]
# **Fourth step:** Uses `plotHR` to generate a plot of the calculated heart rates.

# %%
spacemed.plotHR(hr) #x,y labels and title are default strings

# %%
