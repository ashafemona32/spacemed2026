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
# # Session5 - pandas

# %%
import pandas

# %%
print(pandas.__version__)

# %%
#read the dataframe
station_ids = pandas.read_csv(
"../data/Niederschlag_1981-2010_Stationsliste.txt",
delimiter=" *; *",
encoding = "iso-8859-1",
index_col="Stations_id",
engine="python")
#index-col = assign one column as index instead of raw index

# %%
station_ids

# %%
station_ids.columns #check each coulum name

# %%
station_ids.info() #get the data frame information

# %%
station_ids.head() #first five row

# %%
station_ids.tail() # last five row

# %%
station_ids.drop(station_ids.columns[-1], axis=1, inplace=True) #delete (drop) the last column (-1)

# %%
station_ids.columns

# %%
station_ids.iloc[2,0] # iloc = index location[row;column] -> select by index
#remember the index start from 0 but we can change it when we read the data frame

# %%
station_ids.iloc[:5] # act like head

# %%
station_ids.iloc[:,1:3] # all rows, all columns [:,:]

# %%
station_ids.loc[3, "Stationsname"] #loc: select by label

# %%
station_ids.loc[:,"geogr. Breite":"geogr. Laenge"]

# %%
station_ids.loc[:,'Bundesland'] #select all row from column Bundesland

# %%
# group data by 'Bundesland' and sort by 'Stationsname'
# ascending = False or True
station_ids.groupby('Bundesland').count().sort_values("Stationsname") 

# %%
mask = station_ids.Bundesland == "Bayern"
#get bolean data series whether that column Bundesland data is "Bayern"

# %%
type(mask)

# %%
station_ids.Bundesland.iloc[-1]

# %%
bayern = station_ids[mask]

# %%
bayern.loc[17]

# %% [markdown]
# ## Exercise
# * get a list of stations in Berlin
# * figure out the station ID of Alexanderplatz
# * load the 30 year mean precipitation data
#     data/Niederschlag 1981-2010.txt
# * only keep the columns with the monthly means

# %% [markdown]
# ### Step1: get a list of stations in Berlin

# %%
bse = station_ids.Bundesland == "Berlin" 

# %%
berlin = station_ids[bse] # list of stations in Berlin

# %% [markdown]
# ### Step2: found Alexanderplatz and got the id

# %%
berlin # just serach and got the id (399)

# %% [markdown]
# ### Step3: load the 30 years mean precipitation data

# %%
precip_ref = pandas.read_csv(
"data/Niederschlag_1981-2010.txt",
delimiter=" *; *",
encoding = "iso-8859-1",
index_col="Stations_id",
engine="python")

# %%
precip_ref

# %% [markdown]
# ### Step4: only keep the columns with the monthly means

# %%
#select all row for each month
precip_ref = precip_ref.loc[:,"Jan.":"Dez."]

# %%
precip_ref.loc[399].plot.bar()

# %% [markdown]
# ---

# %%
# cehck precipitation of Alexanderplatz
precip = pandas.read_csv(
"data/produkt_precipitation_399_akt.txt",
delimiter=" *; *",
encoding = "iso-8859-1",
engine="python")

# %%
precip.head()

# %%
precip["date_time"] = pandas.to_datetime(precip.MESS_DATUM, format="%Y%m%d%H") 
#transform mess_datun into clearer form

# %%
precip["date_time"]

# %%
precip.head()

# %%
precip_alx = precip[["date_time", "NIEDERSCHLAGSHOEHE"]]

# %%
precip_alx.describe()

# %%
precip_alx.NIEDERSCHLAGSHOEHE.plot()

# %%
precip_alx = precip_alx.rename(columns = {"date_time": "date", "NIEDERSCHLAGSHOEHE": "precipitation"})

# %%
precip_alx.head(20)

# %%
precip_alx = precip_alx.set_index("date")

# %%
precip_alx.plot()

# %%
#go from hourly data to monthly data
monthly = precip_alx.resample("ME").sum() 
# resample(): change the frequency in time series data
# "ME" = Month End

# %%
monthly # this is the recent precipitation

# %%
monthly.describe()

# %%
precip_ref #this is the 30 years mean precipitation 

# %%
precip_ref.loc[399] #select data only from Alexanderplatz using ID

# %%
monthly.groupby(monthly.index.month).describe()

# %%
monthly.plot()

# %%
refs = pandas.DataFrame(
{"precipitation":
precip_ref.loc[399].to_list()*11}, # creat a reference for 11 years by repeat the data 11 times
index = pandas.date_range(
"2015-01-01", "2025-12-31", freq="ME"))

# %%
monthly["climate"] = refs

# %%
monthly.plot()

# %%
monthly["anomaly"] = monthly.precipitation - monthly.climate

# %%
monthly.anomaly.plot()

# %%
# the example from slides
import numpy
from matplotlib import pyplot
fig, axs = pyplot.subplots(1, figsize=(10,8))
monthly[["climate", "precipitation"]].plot(ax=axs)
axs.set_title("precipitation Berlin, Alexanderplatz")
