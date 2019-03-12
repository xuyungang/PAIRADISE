script_location=$1
python_location="$(which python)"
R_location="$(which R)"
ASASCountDir=$2
AStype=$3

mkdir -p ${ASASCountDir%/}/pairadise_result ${ASASCountDir%/}/pairadise_result_raw ${ASASCountDir%/}/pairadise_results_totalcount \
${ASASCountDir%/}/pairadise_results_totalcount10_diff5 ${ASASCountDir%/}/pairadise_results_totalcount10_diff5_FDR \
${ASASCountDir%/}/pairadise_results_totalcount10_diff5_FDR10

#Run PAIRADISE
${R_location} CMD BATCH --no-save --no-restore "--args "${ASASCountDir%/}"/ASAS.SNP."${AStype}".JunctionReadsOnly.byPair.unfiltered.txt "${ASASCountDir%/}"/pairadise_result_raw/"${AStype}"_allexons.txt" {$script_location%/}/PAIRADISE_fast.R

#Run PAIRADISE filters
${python_location} ${script_location%/}/id2gene.py ${ASASCountDir%/}/ASAS.SNP.${AStype}.JunctionReadsOnly.byPair.unfiltered.txt.individualFilter.txt ${ASASCountDir%/}/pairadise_result_raw/${AStype}_allexons.txt ${ASASCountDir%/}/pairadise_result/${AStype}_allexons.txt 0 1 '[^ "\n]+' 3
${python_location} ${script_location%/}/count.py ${ASASCountDir%/}/pairadise_result/${AStype}_allexons.txt ${ASASCountDir%/}/pairadise_results_totalcount/${AStype}_allexons_count.txt
awk '($14>=10) && ($15>=10) && (($13>=0.05) || ($13<=-0.05))' ${ASASCountDir%/}/pairadise_results_totalcount/${AStype}_allexons_count.txt > ${ASASCountDir%/}/pairadise_results_totalcount10_diff5/${AStype}_allexons_count.txt
${python_location} ${script_location%/}/FDR.py ${ASASCountDir%/}/pairadise_results_totalcount10_diff5/${AStype}_allexons_count.txt ${ASASCountDir%/}/pairadise_results_totalcount10_diff5_FDR/${AStype}_allexons_count.txt
awk '($16<=0.1)' ${ASASCountDir%/}/pairadise_results_totalcount10_diff5_FDR/${AStype}_allexons_count.txt >${ASASCountDir%/}/pairadise_results_totalcount10_diff5_FDR10/${AStype}_allexons_count.txt


