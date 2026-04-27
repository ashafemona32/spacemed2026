def plotHR(hr, xlabel="time [s]", ylabel="Heart Rate [BPM]", title="Heart Rate"):
 from matplotlib import pyplot
 pyplot.plot(hr)
 pyplot.xlabel(xlabel)
 pyplot.ylabel(ylabel)
 pyplot.title(title)
 pyplot.show()

