#!/bin/bash

script_dir=$(cd $(dirname $BASH_SOURCE); pwd)
echo "source ${script_dir}/commands.sh" >> ~/.bashrc 
