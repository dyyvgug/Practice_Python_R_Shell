#!/bin/bash

# get the file name
Folder_A="/g/github/practice_shell"  
for file_a in ${Folder_A}/*
do  
    temp_file=`basename $file_a`  
    echo $temp_file
    printf '\n'  
done

# remove the suffix
for file_b in ${Folder_A}/*
do  
    temp_file=`basename $file_b  .sh`  
    echo $temp_file  
    printf '\n'
done

# input 
echo -e "The current path is${PWD},\ninput the target folder path:"  
read InputDir  
echo "${InputDir}"  
echo -e "Please enter the destination output file path:${PWD}"  
read OutputFile    

: > $OutputFile 
for file_c in ${InputDir}/*
 do  
    temp_file=`basename $file_c  .sh`  
    echo $temp_file >> $OutputFile  
done
