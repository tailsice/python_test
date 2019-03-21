#!/bin/bash

Video_DIR="/home/icl/Video"
Convert_DIR="/home/icl/Video2"
LIST_FILE="NAME"
TMP_FILE="check"

LIST=`cat URL`
for i in $LIST
do
  echo $i
  rm -rf $TMP_FILE &> /dev/null
  ./getVideoURL.py $i > $TMP_FILE
  Video_NAME=$(cat $TMP_FILE | grep "番號:" | cut -d ":" -f 2 | sed 's/^[ \t]*//g')
  echo "$Video_NAME:$i" >> $LIST_FILE
  rm -rf $TMP_FILE &> /dev/null
  sleep 5
done
