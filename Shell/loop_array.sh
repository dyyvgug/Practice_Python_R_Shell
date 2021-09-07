#!/bin/bash
#learning loop array in Shell

numbers=('32234' '5883492' '43984' '12454' '84732' '63282')
for item in ${numbers[@]}
do
echo ${item}
done

echo "Get array elements"

i=0
until [ ! $i -lt 5 ]
do
echo "position $i is ${numbers[$i]} "
echo "next position `expr $i + 1` is ${numbers[`expr $i + 1`]}"
i=`expr $i + 1`
done
