#/bin/bash 
#$ -S /bin/bash                   
#$ -R y                                   
#$ -pe shared 8
#$ -l h_data=4G,h_rt=15:00:00
#$ -V       
#$ -cwd
#$ -j y
#$ -m bea

CountsFile=$1
R_location="$(which R)"
echo ${R_location} CMD BATCH --no-save --no-restore "--args "${CountsFile%/}" "${CountsFile%/} PAIRADISE_fast.R
${R_location} CMD BATCH --no-save --no-restore "--args "${CountsFile%/}" "${CountsFile%/}  PAIRADISE_fast.R
