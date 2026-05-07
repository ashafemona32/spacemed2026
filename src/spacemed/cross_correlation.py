from matplotlib import pyplot
from pathlib import Path
from matplotlib import pyplot
import spacemed
import argparse
import numpy
from .__version__ import __version__
import nibabel
import pandas
import seaborn
import numpy
import scipy.signal


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=Path, help="name of fMRI file")
    parser.add_argument("-s", "--slice",type=int, help = "the slice to process (an integer)"
    parser.add_argument("-o", "--output",
                        type=Path, help="the name of the output image file")
    
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser

def main():
    parser = arg_parser()
    args = parser.parse_args()

    fmri = nibabel.load(args.data)
    nt = fmri.shape[-1]
    fmri_data = fmri.get_fdata()
    z = args.slice - 1
    
    s_one = numpy.array([1]*5 + [0]*5)
    signal = numpy.tile(s_one, int(numpy.ceil(nt/10)))[:nt]
    

    corr_map = numpy.zeros(fmri.shape[:2])
    
    background_threshold = 250
    for x in range(corr_map.shape[0]):
        for y in range(corr_map.shape[1]):
            time_series = fmri_data[x,y,z, :]
            if numpy.mean(time_series) < background_threshold: 
                corr_map[x, y] = 0
                continue
            cross, lag, p = spacemed.fmriCross(signal, fmri_data, (x,y,z))
            corr_map[x,y] = numpy.max(cross)

    brain = numpy.mean(fmri_data[:,:,z,:], axis = -1)
    overlap_map = numpy.copy(corr_map)
    
    fig, axes = pyplot.subplots(1)
    axes.imshow(brain.T,origin="lower",cmap="grey")
    axes.imshow(overlap_map.T,origin="lower",cmap="viridis", alpha = 0.5) 

    pyplot.savefig(args.output)

if __name__ == "__main__":
    main()
