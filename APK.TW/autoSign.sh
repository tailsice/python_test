#!/bin/bash

DIR="/home/icl/APK.TW"

cd $DIR
./getRawData.py > RAW
URL=$(cat RAW | grep amupper | grep href | cut -d "'" -f 2)
./sign.py "$URL"
