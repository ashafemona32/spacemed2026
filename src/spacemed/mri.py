import numpy
import scipy.signal


def normalise(data):
    norm = data - numpy.mean(data)
    norm = norm / numpy.std(data)
    return norm


def fmriCross(input_sig, output_fmri, voxel_num):
    time_series = output_fmri[voxel_num]

    cross = scipy.signal.correlate(
        normalise(time_series), normalise(input_sig), mode="same"
    )

    lags = scipy.signal.correlation_lags(
        len(time_series), len(input_sig), mode="same")

    loc_p = numpy.argmax(cross)

    return cross, lags, loc_p
