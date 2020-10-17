#! /usr/bin/env bash

declare -a etacuts=(2.6 3.1 3.6 4.1)
declare -a mmjjcuts=(750 1000 1250 1500 1750 2000)
temp=./current_script.ma5

for ecut in ${etacuts[@]};
	do
	for mcut in ${mmjjcuts[@]};
		do
    		cp disc_contour_jet_select_opt.ma5 $temp
    		sed -i "" s/ETACUT/$ecut/g $temp
		sed -i "" s/MJJCUT/$mcut/g $temp
    		sed -i "" s/FILENAME/disc_contour_sdEta_L1pt8TeV${ecut}_mjj${mcut}/g $temp 
    		python2.7 ../../../HEPTools/madanalysis5/madanalysis5/bin/ma5 -s $temp
	done
done