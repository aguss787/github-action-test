#!/usr/bin/env bash

tar -xvf test.tar.gz
ls -R

tar -xvf test.tar.gz -O '*/setup.py'
