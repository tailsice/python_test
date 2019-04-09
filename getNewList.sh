#!/bin/bash
FILE1="old_url"
FILE2="new_url"
FILE3="download_url"

if [ -e $FILE3 ]; then
  rm -rf $FILE3
fi

LIST=$(cat $FILE2)
for i in $LIST
do
  grep $i $FILE1 &> /dev/null
  if [ "$?" != "0" ]; then
    echo $i >> $FILE3
  fi
done
