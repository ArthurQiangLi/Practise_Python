#!/bin/bash

cd ../
if [ -d build ]; then #check if /build exists, delete it first.
  rm -r build
fi
cd ../
pwd
cd a2 && mkdir build && cd build && cmake ../ && make #run the professor's grading  command
cd ../test #go back to /test, because we was at /build in last line.

#If you don't want to comiple the executable, just delete all lines above.

echo "" > test.log # Clear the log file first
counter=1

for infile in ../test/t*.in; do
    echo -e "\n------------------------------------------" >> test.log
    echo -e "\t No.$counter, testing $(basename $infile)" >> test.log
    echo "------------------------------------------" >> test.log
    echo "<<<<input is:>>>>" >> test.log
    cat $infile >> test.log
    
    echo -e "\n<<<<output is:>>>>\n" >> test.log
    ../build/ece650-a2 < $infile >> test.log
    ((counter++))
done
