#!/bin/bash

./stokes $1 $2 $3
/home/maksim/CLionProjects/NIR/env/bin/python3.11 /home/maksim/CLionProjects/NIR/scripts/solution.py /home/maksim/CLionProjects/NIR/src/A.mtx /home/maksim/CLionProjects/NIR/src/b.txt
./stokes_grid solution.txt $1 $2
