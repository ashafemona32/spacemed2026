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
#     display_name: Python [conda env:conda_envs-computelab-2025-2]
#     language: python
#     name: conda-env-conda_envs-computelab-2025-2-py
# ---

# %% [markdown]
# # Session2
# We are going to use notebooks for some python
# * basic types
# * flow control

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Simple calculation

# %% [markdown]
# * "+" addition
# * "-" substraction
# * "*" multiplication
# * "/" division
# * "**" power
# * "%" modulo — the remainder of a division
# * "//" floor division — divide and round down to the nearest integer
# * "@" matrix multiplication, new in python 3.5

# %%
4 / 2

# %%
4**2

# %%
12 % 4 

# %%
13 % 4

# %%
13 // 4 

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Assign variables_integer

# %%
a = 2

# %%
a

# %%
a*8

# %%
type(a) #find out the type of an object

# %%
#print the documention associated with the type of the object in an ipython environment
# ?a  

# %%
#get a list of all the attributes and methods associated with a type
dir(a) 

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Assign Variables_String

# %%
aString = 'hello, world!'

# %%
stringWithDoubleQ = "I'm not a NPC."

# %%
print(aString)

# %%
aMultiLine = """
This is a long long
sentence. """

# %%
print(aMultiLine)

# %%
aString.capitalize()

# %%
aString.upper()

# %%
aString.split("l")

# %%
aString.replace("hello", "Hola")

# %%
print(aString) #nothing change

# %%
aString = aString.capitalize()
print(aString)

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Change objects' type

# %%
float(1)

# %%
a = 1

# %%
b = 1.5

# %%
c = str(a+b)

# %%
type(c)

# %%
c+1.5 #error bcs c is string now

# %%
#you can multiplize string with int!
aString*2

# %%
#you can add string together
aString + stringWithDoubleQ

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Link sentences together 

# %%
name = "Sammy"
age = "45"

# %%
print("{0} is {1} yeaers old".format(name, age))

# %%
print (f'{name} is 'f'{age} years old.')

# %%
pi = 3.141592653589793
print("The value of pi is {0}.".format(round(pi,3))) # new style

# %%
print(f'The value of pi is {pi:.3f}.') # handy way

# %%
print("The value of pi is %f." %(round(pi,3))) # old way

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## List

# %%
alist = []

# %%
alist.append(28)

# %%
print(alist)

# %%
len(alist)

# %%
alist.append("Sammy")

# %%
len(alist)

# %%
print(alist[0]) # index starts from 0

# %%
alist[1] = "Jack"

# %%
print(alist)

# %%
del alist[0]

# %%
print(alist)

# %%
alist.append(True)

# %%
print(alist)

# %%
alist.remove(True)

# %%
print(alist)

# %%
anotherList = ["Hello", "World", "error"]

# %%
anotherList.remove("error")

# %%
anotherList

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Call elements from the list

# %%
number = [1,2,3,4,5]

# %%
number[0:2]

# %%
number[:4]

# %%
number[0:]

# %%
number[0::2]

# %%
number[::-1]

# %%
number[-3]

# %%
number[0:6]

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Dictionary

# %%
aDict = {}

# %%
aDict["key"] = "world"

# %%
aDict["key"]

# %%
aDict[1] = 100

# %%
aDict

# %%
planet = {
    "Earth" : 1 ,
    "Moon" : 0.16,
    "Mars" : 0.38
}

# %%
planet

# %%
p = "Moon"

# %%
print(f'The gravity of planet {p} is {planet[p]}!')

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# ## Flow control

# %% [markdown]
# ### loop

# %%
for i in range(10):
    print(i)

# %%
planetList = ["Earth", "Jupiter", "Mars"]

# %%
for x in planetList:
    print(x, len(x))

# %%
# use loop for a dictionary, then it will print the keys
for p in planet:
    print(p)

# %%
for p in planet:
    print(f'The gravity of {p} is {planet[p]}.')

# %% [markdown]
# ### condition

# %%
p = "Mars"

# %%
if planet[p] > 1:
    print(f'{p} has a lager gravity than the Earth.')
elif planet[p] < 1:
    print(f'{p} has a less gravity than the Earth.')
else:
    print(f'{p}has the same gravity as the Earth.')

# %%
p = "Earth"

# %%
if planet[p] > 1:
    print(f'{p} has a lager gravity than the Earth.')
elif planet[p] < 1:
    print(f'{p} has a less gravity than the Earth.')
else:
    print(f'{p} has the same gravity as the Earth.')

# %% [markdown]
# ### Application

# %%
#use loop and condition together!
for p in planet:
    if planet[p] > 1:
        print(f'{p} has a lager gravity than the Earth.')
    elif planet[p] < 1:
        print(f'{p} has a less gravity than the Earth.')
    else:
        print(f'{p} has the same gravity as the Earth.')
