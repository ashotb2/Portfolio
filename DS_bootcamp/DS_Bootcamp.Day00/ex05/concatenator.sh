#!/bin/sh

search="ls *.csv"
output=concat.csv

if [ -z "$($search 2>/dev/null)" ]; then
    search="ls ex05/*.csv"
    output=ex05/concat.csv
fi

partition_files=$($search)
file_1=$($search | head -n 1)
header=$(head -n 1 $file_1)
echo $header > $output

for file in $partition_files; do
    tail -n +2 $file >> $output
done