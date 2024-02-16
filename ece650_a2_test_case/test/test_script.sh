#!/bin/bash

echo "" > test.log # Clear the log file first
counter=1

for infile in ../test/t*.in; do
    echo "---------------------" >> test.log
    echo "No.$counter, testing $(basename $infile)" >> test.log
    echo "input is:" >> test.log
    cat $infile >> test.log
    
    echo -e "\noutput is:\n" >> test.log
    ../build/ece650-a2 < $infile >> test.log 2>&1 #output cout and cerr both to the log file.
    echo -e "\n---------------------" >> test.log
    ((counter++))
done
