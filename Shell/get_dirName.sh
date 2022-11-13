#!/bin/bash

ls -l ./ |awk '/^d/ {print $NF}' > dirName.txt

cat dirName.txt | while read line
do
        echo $line
        cd /home/hello/$line/dir1/dir2/
        ls *.txt
done
