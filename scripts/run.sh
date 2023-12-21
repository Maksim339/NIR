#!/bin/bash

/home/maksim/CLionProjects/NIR/env/bin/python3.11 /home/maksim/CLionProjects/NIR/scripts/strokes.py $1 $2 $3
/home/maksim/CLionProjects/NIR/env/bin/python3.11 /home/maksim/CLionProjects/NIR/scripts/solution.py
/home/maksim/CLionProjects/NIR/env/bin/python3.11 /home/maksim/CLionProjects/NIR/scripts/strokes_grid.py solution.txt $1 $2
