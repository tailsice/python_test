#!/bin/bash

Video_DIR="/home/icl/Video"
Convert_DIR="/home/icl/Video2"

LIST=`ls -t $Video_DIR`
for i in $LIST
do
  echo $i
  /home/icl/ffmpeg/ffmpeg -i $Video_DIR/${i} -f mp4 -vcodec libx264 -preset fast -profile:v main -acodec aac $Convert_DIR/${i} -hide_banner
  rm -rf $Video_DIR/$i 
done
