#!/bin/bash
# bash traverse_del.sh ./ *.sam

function scandir() {
    local cur_dir parent_dir workdir
    workdir=$1
    cd ${workdir}
    if [ ${workdir} = "/" ]
    then
        cur_dir=""
    else
        cur_dir=$(pwd)
    fi
 
    for dirlist in $(ls ${cur_dir})
    do
        if test -d ${dirlist};then
            cd ${dirlist}
            scandir ${cur_dir}/${dirlist} $2
            cd ..
        else
            #echo ${cur_dir}/${dirlist}
            # do what you want
            local filename=$dirlist
            #echo "current folder："$filename
            #echo ${#2} #.zip 4
            #echo ${filename:(-${#2})}

        	if [[ ${filename:(-${#2})} = $2 ]] 
        	then
        		echo "delete "$filename
 				rm -f $filename
                # echo "copy" $filename
                # copy $filename /home/hello
 			fi
        fi
    done
}
 
if test -d $1
then
    scandir $1 $2
elif test -f $1
then
    echo "you input a file but not a directory,pls reinput and try again"
    exit 1
else
    echo "the Directory isn't exist which you input, input a new one"
    exit 1
fi

