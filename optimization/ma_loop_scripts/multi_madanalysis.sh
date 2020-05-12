#! /usr/bin/env bash

declare -a etacuts=(2.6 3.1 3.6 4.1 4.6 5.1 5.6 6.1)
declare -a mmjjcuts=(120 500 750 1000)
declare -a ptacuts=(100 150 200 250 300 350 400 450 500)
declare -a maacuts=(200 250 300 350 400 450 500 550 600 650 700)
temp=./current_script.ma5

for ptcut in ${ptacuts[@]};
	do
	for mcut in ${maacuts[@]};
		do
    		cp axion_optimization_sdEta_maa_pta.ma5 $temp
    		sed -i "" s/ETACUT/'3.6'/g $temp
    		sed -i "" s/PTCUT/$ptcut/g $temp
		sed -i "" s/MAACUT/$mcut/g $temp
    		sed -i "" s/FILENAME/analysis_tight_pta${ptcut}_maa${mcut}/g $temp 
    		python2.7 ../../HEPTools/madanalysis5/madanalysis5/bin/ma5 -s $temp
	done
done
