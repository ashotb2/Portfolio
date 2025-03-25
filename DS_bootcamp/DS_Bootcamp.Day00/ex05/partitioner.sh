#!/bin/sh

flag=true
input=../ex03/hh_positions.csv

if [ ! -f $input ]; then
    input=ex03/hh_positions.csv
    flag=false
fi

header=$(head -n 1 $input)
dates=$(tail -n +2 $input | cut -d, -f2 | cut -dT -f1 | sort | uniq)
for date in $dates; do
    output_file="${date}\".csv"
    if [ $flag = false ]; then
        output_file="ex05/$output_file"
    fi
    echo "$header" > "$output_file"
    grep "$date" "$input" >> "$output_file"
done