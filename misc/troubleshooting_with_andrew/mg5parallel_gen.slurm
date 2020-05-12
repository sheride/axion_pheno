#!/bin/bash
#SBATCH --mail-user=elijah.sheridan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=7-00:00:00
#SBATCH --mem=8G
#SBATCH --array=0-0
#SBATCH --job-name=MG_AxionSignalGurrolaCuts1GeV
#SBATCH --output=MG_AxionSignalGurrolaCuts1GeV_%A_%a.out

# Define the path to your home directory
home=/home/sheride

# Enter the name of the <ProcDirectory>
procdirectory=AxionSignal

# Define the label or processtag
processtag=axion_signal_gurrola_cuts_1gev

# Define the number of events you want to generate in this run:
nevents=1000000

# Load the necessary modules.
source /etc/profile.d/lmod.sh
module load GCC/6.4.0-2.28
module load OpenMPI/2.1.1

echo "Generating LHE samples with gridpack for ${procdirectory}..."

# Define the path to the gridpack: 
pathtogridpack=${home}/gridpacks_${procdirectory}/${processtag}

# Create a directory where your LHE files will be stored
mkdir -p ${home}/gridpacks_${procdirectory}/outputlhe_${processtag}

# Define a function that can clean up the working area in case the job fails or when it ends.
trap "rm -rf $localdir" EXIT

tmp_cleaner()
{
rm -rf ${localdir}
exit -1 
}
trap ’tmp_cleaner’ TERM

# Define the name of your directory in /tmp. "processtag" refers to a label for 
# the specific process contained in the gridpack. 
localdir=/tmp/${processtag}_${SLURM_JOBID}

# Create a unique directory on compute node
echo "Creating a unique directory on the temporary area of this node..." 
mkdir ${localdir}
echo "Done."

echo "ls..."
echo "$(ls)"

# Move to that directory
cd ${localdir}
echo "Current directory: $PWD"

#Run program that reads/writes to/from local disk
echo "Copying and unpacking the gridpack to the current location..." 
cp ${pathtogridpack}/run_01_gridpack.tar.gz .
tar -xzvf run_01_gridpack.tar.gz
rm run_01_gridpack.tar.gz
echo "Done."

echo "Starting the event generation..." 
./run.sh ${nevents} ${SLURM_JOBID}
echo "Done."

echo "ls ..."
ls

# Change the name of the output file, so when you store it the output directory,
# it does not overwrite the other files.
echo "Moving the LHE file "events.lhe.gz" to events_$SLURM_JOBID.lhe.gz... "
mv events.lhe.gz events_$SLURM_JOBID.lhe.gz
echo "Done."

# Move results to working directory on GPFS
echo "Copying the file events_$SLURM_JOBID.lhe.gz to the working directory"
cp events_$SLURM_JOBID.lhe.gz ${home}/gridpacks_${procdirectory}/outputlhe_${processtag} 
echo "Done."

echo "Job completed."
