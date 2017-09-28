#!/bin/bash
function_one () {
for x in $*
do
	if [ $# -gt 3 ]
	then
	echo ______
	echo $x "single"
	echo $* "all"
	echo $# "total number"
	echo $(seq 1 $#) 
	echo $0
	fi
done
}

function_one test test2 test3 test4
