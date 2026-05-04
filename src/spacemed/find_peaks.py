import numpy


def findPeaks(time, absorption, w=50):
    w = w
    peaks = []
    for i in range(len(absorption)):
        start = max(i - w, 0)
        end = min(i + w, len(absorption))
        window = absorption[start:end]
        max_pos = numpy.argmax(window) + start
        if i == max_pos:
            peaks.append(i)
    return peaks
