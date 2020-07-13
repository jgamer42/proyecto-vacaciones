#!/bin/bash
set -o pipefail
set -e
cd .. 
for folder in */; do
    echo "$folder"
    cd "$folder"
    ls
    git rm __pycache__
    cd ..
done 