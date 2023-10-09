#!/bin/bash

sudo apt install -y tldr bash-completion &

cat << EOF >> ~/.bashrc
source /etc/profile.d/bash_completion.sh

# Setup color
force_color_prompt=yes
export PS1="\033[36m\u\033[35m @ \033[36m\h\033[35m [ \033[32m\w \033[35m]\033[32m \$? \033[37m  \n$ "

# Aliases
alias ls="ls --color -A --group-directories-first"
alias ll="ls --color -lathr --group-directories-first"
alias l.="ls -d .* --color --group-directories-first"
alias grep="grep --color"
alias c..="cd ../.."
alias untar="tar -zxvf"
alias nao="sudo reboot now"
alias py="/usr/bin/python3"
EOF

source ~/.bashrc

cat << EOF >> ~/.vimrc
" Ricing
set number
set rnu
set cuc 
hi CursorColumn ctermbg=16
set cursorline
hi CursorLineNR ctermbg=16
EOF
