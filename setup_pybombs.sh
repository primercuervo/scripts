#!/bin/sh/
# This script is intended to be run just after I install my own configuration
# from https://github.com/primercuervo/dotfiles
# It helps me set up an RFNoC PyBombs prefix to work on RFNoC development
# With Ettus Research Devices

# Retrieve the amount of cores available in the current machine
CORES=grep -c ^processor /proc/cpuinfo

sudo pip install --upgrade git+https://github.com/gnuradio/pybombs.git
pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git
pybombs recipes add gr-etcetera git+https://github.com/gnuradio/gr-etcetera.git
pybombs recipes add ettus git+https://github.com/EttusResearch/ettus-pybombs.git
if [ ! -d ~/src/rfnoc/ ]; then
    mkdir -p ~/src/rfnoc
fi
pybombs --config makewidth=$CORES prefix init ~/src/rfnoc -R rfnoc -a rfnoc

source ~/src/rfnoc/setup_env.sh
