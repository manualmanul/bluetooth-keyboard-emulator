#!/usr/bin/env

echo 'Initializing Croncuts'
echo

echo 'Installing dependencies'
apt update
apt-add-repository universe
apt install bluez git python3 python3-pip bluez-utils -y

echo 'Installing pip3 dependencies'
pip3 install pynput dbus-python

echo 'Cloning SySS-Research/bluetooth-keyboard-emulator'
git clone https://github.com/SySS-Research/bluetooth-keyboard-emulator.git

echo 'Setting up SySS-Research/bluetooth-keyboard-emulator'
cd bluetooth-keyboard-emulator
sudo ./setup.sh

echo 'Starting bluetooth keyboard emulator'
sudo ./start.sh

echo 'Attaching to tmux'
sudo tmux attach -t kbdemu
