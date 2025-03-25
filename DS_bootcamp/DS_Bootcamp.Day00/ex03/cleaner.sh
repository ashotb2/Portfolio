#!/bin/sh

output=hh_positions.csv
input=../ex02/hh_sorted.csv

if [ ! -f $input ]; then
    output=ex03/hh_positions.csv
    input=ex02/hh_sorted.csv
fi
awk -F, 'BEGIN {OFS=","} 
NR == 1 {print $0; next}
{
    new_value = "\""
    if (tolower($3) ~ /junior/) {
        new_value = new_value "Junior"
    }
    if (tolower($3) ~ /senior/) {
        if (new_value != "\"") {
            new_value = new_value "/Senior"
        } else {
            new_value = new_value "Senior"
        }
    }
    if (tolower($3) ~ /middle/) {
        if (new_value != "\"") {
            new_value = new_value "/Middle"
        } else {
            new_value = new_value "Middle"
        }
    }
    new_value = new_value "\""
    if (new_value == "\"\"") {
        new_value = "\"-\""
    }
    $3 = new_value
    print $0  # Print the modified line
}' $input > $output