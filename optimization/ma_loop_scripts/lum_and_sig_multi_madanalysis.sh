#! /usr/bin/env bash

declare -a etacuts=(2.6 3.6)
declare -a lumis=(40 150 3000)
declare -a ratios=(0 0.1 0.15 0.25)
temp=./current_script_lumi_ratio.ma5

for ecut in ${etacuts[@]};
	do
	for lumi in ${lumis[@]};
		do
		for ratio in ${ratios[@]};
			do
    			cp lumi_and_sig_metric.ma5 $temp
    			sed -i "" s/ETACUT/$ecut/g $temp 
    			sed -i "" s/LUMI/$lumi/g $temp
			sed -i "" s/RATIO/$ratio/g $temp
    			sed -i "" s/FILENAME/analysis_deltaeta${ecut}_lumi_${lumi}_ratio_${ratio}/g $temp 
    			python2.7 ../../HEPTools/madanalysis5/madanalysis5/bin/ma5 -s $temp
		done
	done
done
