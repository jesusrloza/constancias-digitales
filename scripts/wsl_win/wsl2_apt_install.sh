#!/usr/bin/sh
sudo apt update -y && sudo apt upgrade -y

# Append my bashrc configurations
cat ./bashrc_jesusrloza >> ~/.bashrc
source ~/.bashrc

# CLI programs
sudo apt-get install openssl qrencode poppler-utils -y
sudo apt-get install git neovim neofetch ranger htop curl tree -y
sudo apt-get install python3 python3-pip sqlite3 jupyter -y
sudo apt-get remove nano -y

# Pip config for Data Analysis
pip3 install -U pip notebook psutil openpyxl # youtube-dl
pip3 install -U numpy pandas scikit-learn matplotlib seaborn nltk beautifulsoup4

# Jupyter notebook config modification to fix behaviour on windows
jupyter notebook --generate-config
old_jn="#c.NotebookApp.use_redirect_file = True"
new_jn="c.NotebookApp.use_redirect_file = False"
sed -i "s/$old_jn/$old_jn\n$new_jn/g" /home/$USER/.jupyter/jupyter_notebook_config.py

# Add an alias on WSL to cd into the Windows User Directory
alias_start='# Some useful aliases - jesusrloza'
cdwin="    alias cdwin='cd \$(wslpath "'"$(wslvar USERPROFILE)"'"'"
sed -i "s/$alias_start/$alias_start\n$cdwin/g" /home/$USER/.bashrc
