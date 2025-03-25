#!/bin/sh

if [ -z "$1"]; then
    echo "Usage: $0 <vacancy_id>"
    exit 1
fi

VACANCY_ID=$1
OUTPUT_FILE="hh.json"

curl "https://api.hh.ru/vacancies?text=$VACANCY_ID&per_page=20" | jq '.' > $OUTPUT_FILE

echo "Success"