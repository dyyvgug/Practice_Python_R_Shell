#!/bin/bash

oldsuffix="gff"
newsuffix="txt"
dir=$(eval pwd)

for file in $(ls $dir | grep .${oldsuffix})
    do
        name=$(ls ${file} | cut -d. -f1)
        gff3ToGenePred -warnAndContinue $file ${name}.${newsuffix}
    done


