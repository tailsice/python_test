#!/bin/bash

FFMPEG="/home/icl/ffmpeg/ffmpeg"
TMP_FILE="/tmp/FILE"
DIR="/home/icl/Video3"
#i="/play/vzSOM21rHSGCt%2BJd"

LIST=$(cat URL)
for i in $LIST
do
  ./getVideoURL.py $i > $TMP_FILE
  URL=$(cat $TMP_FILE | grep playlist | tail -n 1 | cut -d "\"" -f 2)
  FILE_NAME=$(cat $TMP_FILE | grep playlist | tail -n 1 | cut -d "\"" -f 2 | cut -d "/" -f 7)
  echo "URL = $URL"
  echo "FILE NAME = $FILE_NAME"
  $FFMPEG -protocol_whitelist "file,http,https,tcp,tls" -i "$URL" -c copy "$DIR/$FILE_NAME.mp4"
done

#ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i "將m3u8網址貼上到這邊" -c copy "你想儲存的檔案路徑/test.mp4"
