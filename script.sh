#!/bin/bash

#Opening the folder
cd ~/Downloads/spark-1.1.0

#Starting spark server
./sbin/start-all.sh

#CAlculating profit for each file
((i=0))
while((i<10))
do
  python shop.py
  ./bin/spark-submit mapred.py
  ((i=i+1))
done

#Plotting a graph
python graphmatplot.py

#Closing server
./sbin/stop-all.sh
  
