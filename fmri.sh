#!/bin/bash
#SBATCH --job-name="Name of the Job"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00
#SBATCH --output=logs/plotfmri_%j.out
#SBATCH --array=1-32

#the program we are running
echo "starting job ${SLURM_ARRAY_TASK_ID}"
sm_plot_fmri "fmri-data/3_fMRI_TR2sec_3mm_3min.nii" -s ${SLURM_ARRAY_TASK_ID}  -o "fmri-data/fMRI_slice_${SLURM_ARRAY_TASK_ID}.png"
echo done

