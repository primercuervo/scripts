#!/usr/bin/env/ bash

# TODO: make it a complete dotfile (and move it to dotfiles)

# Following the link at:
# https://github.com/ipython-contrib/jupyter_contrib_nbextensions#installation
sudo pip install jupyter_contrib_nbextensions
sudo pip3 install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
sudo pip install jupyter_nbextensions_configurator
sudo pip3 install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user

# Steps to add and activate the vim binding
mkdir -p $(jupyter --data-dir)/nbextensions
cd $(jupyter --data-dir)/nbextensions
git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
chmod -R go-w vim_binding

echo read the file for customization
# https://github.com/lambdalisue/jupyter-vim-binding/wiki/Customization
# That didnt work, gotta use the solution I upvoted here:
# https://stackoverflow.com/questions/22843891/turn-off-auto-closing-parentheses-in-ipython

