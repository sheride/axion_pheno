#! /usr/bin/env bash

for f in ../diphoton_double_isr_background_data/merged_lhe/*.lhe ; do tar -czvf "${f}.gz" "$f" > "${f}.gz" ; done

