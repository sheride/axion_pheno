#! /usr/bin/env bash

declare -a lumis=(40 150 1000 2000 3000)
temp=./current_script.ma5


for lumi in ${lumis[@]};
	do
    	cp luminosity_probe_four_cuts.ma5 $temp
    	sed -i "" s/LUMI/$lumi/g $temp
    	sed -i "" s/FILENAME/four_cuts_lum${lumi}/g $temp 
    	python2.7 ../../HEPTools/madanalysis5/madanalysis5/bin/ma5 -s $temp
	done
