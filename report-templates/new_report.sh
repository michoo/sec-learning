#!/bin/bash

time_stamp=$(date +%Y-%m-%d-%T)
mkdir -p "${time_stamp}"
cp -r ./backup/* "./${time_stamp}/"