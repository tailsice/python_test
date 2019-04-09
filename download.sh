#!/bin/bash

Video_DIR="/home/icl/Video"
Video_File="DATA"

LIST=$(cat NAME2)
for i in $LIST
do
#  echo $i
  Video_NAME=$(echo $i | cut -d "@" -f 1)
  URL=$(echo $i | cut -d "@" -f 3)
  echo "Video Name = $Video_NAME"
  echo "Video URL = $URL"
  ./getVideoURL.py $URL > $Video_File
  Video_URL=$(cat $Video_File | grep streamlink.exe | cut -d "\"" -f 4 )
#  Video_NAME=$(cat $Video_File | grep "番號:" | cut -d ":" -f 2 | sed 's/^[ \t]*//g')
  /usr/bin/streamlink --hls-segment-threads 10 "$Video_URL" best -o $Video_DIR/${Video_NAME}.mp4
done
