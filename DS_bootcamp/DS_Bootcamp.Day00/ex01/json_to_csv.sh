#!/bin/sh
flag=true


if [ ! -f "../ex00/hh.json" ]; then
    jq -r -f ex01/filter.jq ex00/hh.json > ex01/hh.csv
    flag=false
fi

if [ $flag = true ]; then
    jq -r -f filter.jq ../ex00/hh.json > hh.csv
fi