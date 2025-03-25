#!/bin/sh

input=../ex03/hh_positions.csv  
output=hh_uniq_positions.csv

if [ ! -f $input ]; then
    input=ex03/hh_positions.csv
    output=ex04/hh_uniq_positions.csv
fi
awk -F, 'BEGIN {OFS=","} 
NR == 1 {print "\"name\"","\"count\""; next}
{count[$3]++}
END {
    for (name in count) {
        print name, count[name]
    }
}' $input > $output

header=$(head -n 1 $output)
sorted=$(tail -n +2 $output | sort -t, -k2,2nr)
echo "$header" > $output
echo "$sorted" >> $output