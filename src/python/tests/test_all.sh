#!/bin/sh
for f in */ ; do
  cd $f
  python -m unittest discover
  cd ..
done
