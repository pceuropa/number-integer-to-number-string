#!/bin/sh

while inotifywait -r -e modify .
  do
    clear
    ipython $1
  done
