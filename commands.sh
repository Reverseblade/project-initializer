#!/bin/bash

SCRIPT_PATH="$(cd $(dirname $BASH_SOURCE); pwd)"
PROJECT_PATH=
GITHUB_ACCOUNT="Reverseblade"
EDITOR='Visual Studio Code'

function create() { 
    set -e
    cd ${SCRIPT_PATH} 
    if [ ! -d ${PROJECT_PATH}$1 ]; then
        mkdir ${PROJECT_PATH}$1 
        echo "created new directory named $1"
    fi
    if python github_repository_initializer/create_repository.py $1 ; then
        cd ${PROJECT_PATH}$1 
        git init
        echo 'Initialized Git'
        git remote add origin https://github.com/${GITHUB_ACCOUNT}/$1.git
        echo 'Added remote origin'
        touch README.md
        echo '#' $1 > README.md
        git add README.md
        git commit -m "initial commit"
        git push -u origin master
        open -a "${EDITOR}" .
        git checkout -b develop
        echo 'Opened project in editor'
        echo 'Project initialization complete!'
    fi   
}

function create-push-github-repository() {
    PROJECT_NAME=$1
    set -e
    if python ${SCRIPT_PATH}/github_repository_initializer/create_repository.py ${PROJECT_NAME} ; then
        git remote add origin https://github.com/${GITHUB_ACCOUNT}/${PROJECT_NAME}.git
        echo 'Added remote origin'
        # touch README.md
        # echo '#' $1 > README.md
        # git add README.md
        # git commit -m "initial commit"
        git push -u origin master
        echo 'Project initialization complete.'
    fi  
}
