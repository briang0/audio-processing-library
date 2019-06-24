#!/bin/sh
for f in */ ; do
  cd $f
  if [[ $f != *pycache* ]] ;
  then
    for s in $f ; do
      echo $s
      python -m unittest *.py
    done
  fi
  cd ..
done
