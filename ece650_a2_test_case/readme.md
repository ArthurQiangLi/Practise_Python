# Guide for testing a2 automaticlly

## 1.Introduction
All needed files are in `/test`, We use `test_script.sh` to test all the files automatically and log the input+out put gracely in file `test.log`.

## 2.How to use?
1. Make sure you `cd` to `/test` directory.
2. Compile your program `ece650-a2` first.
3. Run `./test_script.sh` and checkout `test.log`.
4. That's it!

## 3.Key notes in the code

```
Note1: You executable is in `../build/` because we have defined `    ../build/ece650-a2 < $infile >> test.log
`, modify it if you have your executable in other place.

echo "" > test.log # Clear the log file first
counter=1

for infile in ../test/t*.in; do
    echo "---------------------" >> test.log
    echo "No.$counter, testing $(basename $infile)" >> test.log
    echo "input is:" >> test.log
    cat $infile >> test.log
    
    echo -e "\noutput is:\n" >> test.log
    ../build/ece650-a2 < $infile >> test.log
    echo -e "\n---------------------" >> test.log
    ((counter++))
done
```