# Welcome to 2026 Course of Data Literacy 

This file uses [markdown](https://www.markdownguide.org/). Checkout the
[cheat sheet](https://www.markdownguide.org/cheat-sheet/) for a summary
of the syntax. GitLab supports various
[Markdown extensions](https://docs.gitlab.com/user/markdown/)

## About me
Hi there, I'm Sammy 👋 I am a Master's student currently specialising in **Space Medicine**.
* Currently based in Germany :de:
* Program: Erasmus
## How to reach me
📬 Email: shan-shan.chen@charite.de 

# In this course we developed a package -- spacemed
`spacemed` is a Python package designed for processing and analyzing medical pulse data.
It provides tools to load raw signal data, detect physiological peaks,and calculate
heart rate metrics.

## Core Functions of spacemed

|Function               |Description                                                    |
|-----------------------|---------------------------------------------------------------|
|`readPulse(file_name)` |Reads a CSV file and returns `time`  and `absorption` lists.   |
|`findPeaks(time, absorption)` |Uses signal processing to identify local maxima (peaks).|
|`calHR(time, peaks)` |Calculates heart rate based on the time intervals between peaks.  |
|`plotHR(hr)` |Plot heart rates with x,y labels and a title.|

## Current version
Current version is `0.0.1`.
