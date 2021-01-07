#!/usr/bin/env

set -e

echo 'Initializing Croncuts'
echo

echo 'Installing dependencies'
apt update
apt-add-repository universe
apt update
apt install bluez git python3 python3-pip tmux -y
apt install bluez-utils -y || apt install bluez-utils -y || true # apt sometimes doesn't immediately find bluez-utils

echo 'Installing pip3 dependencies'
pip3 install pynput dbus-python

echo 'Cloning manualmanul/Croncuts.git'
git clone https://github.com/manualmanul/Croncuts.git

echo 'Setting up manualmanul/Croncuts.git'
cd bluetooth-keyboard-emulator
sudo ./setup.sh

echo 'Starting bluetooth keyboard emulator'
sudo ./start.sh

echo 'Attaching to tmux'
sudo tmux attach -t kbdemu
