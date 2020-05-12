#! /usr/bin/env bash

for f in ./original_lhe/ht_1600_inf/*.gz ; do gunzip -c "$f" > ./"${f%.*}" ; done


