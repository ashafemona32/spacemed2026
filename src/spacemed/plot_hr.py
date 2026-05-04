from matplotlib import pyplot


def plotHR(hr, xlabel="time [s]",
           ylabel="Heart Rate [BPM]", title="Heart Rate"):
    pyplot.plot(hr)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.title(title)
    pyplot.show()
