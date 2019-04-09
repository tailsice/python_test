#!/bin/bash

Video_DIR="/home/icl/Video"
Convert_DIR="/home/icl/Video2"
LIST_FILE="NAME3"
TMP_FILE="/tmp/check"

LIST=`cat old_url`
for i in $LIST
do
#  echo $i
  rm -rf $TMP_FILE &> /dev/null
  ./getVideoURL.py $i > $TMP_FILE
  Video_NAME=$(cat $TMP_FILE | grep "番號:" | cut -d ":" -f 2 | sed 's/^[ \t]*//g')
  Video_URL=$(cat $TMP_FILE | grep streamlink.exe | cut -d "\"" -f 4 )
  echo "$Video_NAME:$Video_URL:$i" >> $LIST_FILE
  rm -rf $TMP_FILE &> /dev/null
  sleep 5
done
