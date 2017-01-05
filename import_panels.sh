#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "USAGE: ${0} <KIDASH_PATH> <ES_URL> <JSON_DIR>"
    exit 1
fi

KIDASH=$1
ES_URL=$2
JSON_DIR=$3

for JSON_FILE in ${JSON_DIR}/*.json;
do
  if [[ "${JSON_FILE}" == *config.json ]]; then
    echo "Skipping ${JSON_FILE}"
    continue
  fi
  echo "Importing ${JSON_FILE}"
  ${KIDASH} -e ${ES_URL} --import $JSON_FILE
done

echo "...[This is the end]..."
