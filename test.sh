#!/usr/bin/env bash

tar -xvf test.tar.gz
ls -R

if [ -n "$CI" ]
then
    extra_flags="--wildcards"
else
    extra_flags=""
fi

tar -xvf test.tar.gz $extra_flags -O '*/setup.py'
echo "kucing kucing di dinding" >> setup.py
