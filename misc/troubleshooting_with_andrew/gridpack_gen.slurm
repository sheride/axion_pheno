#!/bin/bash
#SBATCH --mail-user=elijah.sheridan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --exclusive
#SBATCH --mem=0
#SBATCH --time=2-00:00:00
#SBATCH --job-name=MG_gridpack_AxionSignalGurrolaCuts1GeV
#SBATCH --output=MG_gridpack_AxionSignalGurrolaCuts1GeV.out

# This script generates gridpacks and gets a whole node, therefore we
# can run in run_mode=2 (multicore) to use all the CPUs in the node.

echo "Starting gridpack generation in multicore mode..."

# Load the modules needed by MG5
source /etc/profile.d/lmod.sh
module load GCC/6.4.0-2.28
module load OpenMPI/2.1.1
module load ROOT/6.10.08-Python-2.7.14

# Define the directory for your home MG5 installation:
home=/home/sheride/
homemg5=/home/sheride/MG5_aMC_v2_6_5/

# Enter the name of the <ProcDirectory>
procdirectory=AxionSignal

# Define the label or processtag
processtag=axion_signal_gurrola_cuts_1gev

# Make a directory where the output tarball will be stored. <processtag> must be a good 
# reference to the process this gridpack is going to contain.
echo "Creating a directory where the current gridpack will be stored..."
mkdir -p ${home}/gridpacks_${procdirectory}/${processtag}
echo "Done."

# Define a function that cleans up the area when the job is done.
trap "rm -rf $localdir" EXIT

# Define a function that will clean up the area once the job is done or when the job fails. 
tmp_cleaner()
{
	rm -rf ${localdir}exit -1
}

trap ’tmp_cleaner’ TERM

# Create a directory in the temporary file of the node where the job is running. 
# Define the name of your directory in /tmp. 
localdir=/tmp/${procdirectory}_${SLURM_JOBID}

# Create a unique directory on the computer node.
echo "Creating a unique directory on the temporary area of this node..." 
mkdir ${localdir}
echo "Done."

# Move to the directory.
cd ${localdir}
echo "Current directory: $PWD"

# Copy your MG5 installation to the temporary area
echo "Copying the home MG5 installation to the temporary area..." 
cp -r ${homemg5}/ ${localdir}
echo "Done."
echo "ls..."
echo "$(ls)"
cd ${localdir}/MG5_aMC_v2_6_5/${procdirectory}/
echo "Current directory: $PWD"

# Launch the generation for that process, make sure your Cards are properly updated
# with the desired parameters. The name of the run takes the job ID number as its name.
# The -f option sets the answers to all questions to the default.
echo "Starting the gridpack generation... (./bin/generate_events -f)"
./bin/generate_events  -f
echo "Done!"

# When this step is done, you should have a tarball named run_01_gridpack.tar.gz
# in <ProcDirectory>
echo "$(ls)"
echo "Moving the gridpack to my home area..."
mv run_01_gridpack.tar.gz ${home}/gridpacks_${procdirectory}/${processtag} 
echo "Done."

echo "Job finished."
