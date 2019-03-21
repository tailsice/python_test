#!/bin/bash

Video_DIR="/home/icl/Video"
Convert_DIR="/home/icl/Video2"
Video_File="DATA"

LIST=`cat 1-1000_URL`
for i in $LIST
do
  echo $i
  rm -rf $Video_File
  ./getVideoURL.py $i > $Video_File
  Video_URL=$(cat $Video_File | grep streamlink.exe | cut -d "\"" -f 4 )
  Video_NAME=$(cat $Video_File | grep "番號:" | cut -d ":" -f 2 | sed 's/^[ \t]*//g')
  /usr/bin/streamlink --hls-segment-threads 10 "$Video_URL" best -o $Video_DIR/${Video_NAME}.mp4

#  /home/icl/ffmpeg/ffmpeg -i $Video_DIR/${Video_NAME}.mp4 -f mp4 -vcodec libx264 -preset fast -profile:v main -acodec aac $Convert_DIR/${Video_NAME}.mp4 -hide_banner
#  rm -rf $S_DIR/$i 

done
