#! /bin/sh
#
# run.sh
# Copyright (C) 2019 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.
#


pipenv --python 3.6
pipenv install
pipenv run python3 test1.py
