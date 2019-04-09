#!/bin/bash 

DIR=/home/icl/Video
LIST=$(ls $DIR)

for i in $LIST
do
  OLD_NAME=$(echo $i | cut -d "." -f 1)
  A=$(echo $OLD_NAME | cut -d "-" -f 1)
  B=$(echo $OLD_NAME | cut -d "-" -f 2)
  mv $DIR/$i $DIR/$A-$B.mp4
done

