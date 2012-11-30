#!/bin/bash

if [ ! -d env ];
then
    virtualenv --no-site-packages env
fi

uname_result=$(uname -s) 

if [ "$uname_result" == "Darwin" ];
then
    # this has to be `easy_install`ed on OSX
    echo "Installing readline"
    env/bin/easy_install readline
fi

# install our deps
echo "Installing deps"
env/bin/pip install -r requirements.txt
