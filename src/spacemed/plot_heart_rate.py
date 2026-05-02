from pathlib import Path
from matplotlib import pyplot
import spacemed
import argparse
import numpy
from .__version__ import __version__
from .load_pulse import readPulse # noqa
from .find_peaks import findPeaks # noqa
from .cal_hr import calHR # noqa


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=Path, help="the name of the input file")
    parser.add_argument("-o", "--output",
                        type=Path, help="write output to file")
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()
    time, absorption = spacemed.readPulse(args.data)
    peaks = spacemed.findPeaks(time, absorption)
    hr = spacemed.calHR(time, peaks)

    absorption = numpy.array(absorption)

    frame, fig = pyplot.subplots(3, 1, figsize=(12, 12))

    fig[0].plot(time, absorption, linewidth=1.0)
    fig[0].set_title("1. Raw Absorption signal")
    fig[0].set_xlabel("Time(s)")
    fig[0].set_ylabel("Absorption")

    fig[1].plot(absorption, linewidth=1.0)
    fig[1].plot(peaks, absorption[peaks], "rx", markersize=5)
    fig[1].set_title("2. Absorption with Peaks")
    fig[1].set_xlabel("Time(s)")
    fig[1].set_ylabel("Absorption")

    fig[2].plot(hr)
    fig[2].set_title("3. Heart Rate")
    fig[2].set_xlabel("Time(s)")
    fig[2].set_ylabel("BPM")

    pyplot.tight_layout()

    pyplot.savefig(args.output)


if __name__ == "__main__":
    main()
