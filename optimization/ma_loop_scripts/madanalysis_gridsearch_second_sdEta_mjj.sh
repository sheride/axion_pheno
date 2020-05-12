#! /usr/bin/env bash

declare -a etacuts=(2.6 3.1 3.6 4.1)
declare -a mmjjcuts=(750 1000 1250 1500 1750 2000)
temp=./current_script.ma5

for ecut in ${etacuts[@]};
	do
	for mcut in ${mmjjcuts[@]};
		do
    		cp second_axion_optimization_sdEta_mjj.ma5 $temp
    		sed -i "" s/MAACUT/'500'/g $temp
		sed -i "" s/PTCUT/'300'/g $temp
    		sed -i "" s/ETACUT/$ecut/g $temp
		sed -i "" s/MJJCUT/$mcut/g $temp
    		sed -i "" s/FILENAME/second_analysis_sdEta${ecut}_mjj${mcut}/g $temp 
    		python2.7 ../../HEPTools/madanalysis5/madanalysis5/bin/ma5 -s $temp
	done
done
