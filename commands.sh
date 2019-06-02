#!/bin/bash

INITIALIZER_PATH=~/Code/others/commands/project_initializer/
PROJECT_PATH=~/Code/projects/
GITHUB_ACCOUNT=Reverseblade

function create() {
    cd ${INITIALIZER_PATH} 
    if python create.py $1; then
        if [ -e ${PROJECT_PATH}$1 ]; then
            cd ${PROJECT_PATH}$1 
            git init
            git remote add origin https://github.com/${GITHUB_ACCOUNT}/$1.git
            touch README.md
            echo '#' $1 > README.md
            git add .
            git commit -m "Initial commit"
            git push -u origin master
            code .
            echo 'Success: Successfully created a new project!'
        else
            echo 'Error: project named' $1 'does not exist'
        fi
    fi   
}
