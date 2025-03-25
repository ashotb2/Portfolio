#!/bin/sh

flag=true

if [ ! -f "../ex01/hh.csv" ]; then
    header=$(head -n 1 ex01/hh.csv)
    
    sorted_content=$(tail -n +2 ex01/hh.csv | sort -t, -k2)
    
    echo "$header" > ex02/hh_sorted.csv
    echo "$sorted_content" >> ex02/hh_sorted.csv
    flag=false
fi

if [ $flag = true ]; then
    header=$(head -n 1 ../ex01/hh.csv)
    
    sorted_content=$(tail -n +2 ../ex01/hh.csv | sort -t, -k2)
    
    echo "$header" > hh_sorted.csv
    echo "$sorted_content" >> hh_sorted.csv
fi
