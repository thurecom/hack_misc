#!/bin/bash

for M in 01 02 03 04 05 06 07 08 09 10 11 12
do
	for D in 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
	do
		wget "http://intelligence.htb/documents/2020-${M}-${D}-upload.pdf"
	done
done