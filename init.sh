#!/bin/bash

cd
git clone https://github.com/Pyrestone/jetson-fan-ctl.git
cd jetson-fan-ctl/
sudo ./install.sh

cd
cd OPIN-JetsonNano-public/
sudo rm /etc/automagic-fan/config.json
cp config.json /etc/automagic-fan/
chmod 664 /etc/automagic-fan/config.json

cd
git clone https://github.com/JetsonHacksNano/installSwapfile
cd installSwapfile/
./installSwapfile.sh -s 12

cd
sudo apt install nano
sudo apt install python3-pip
sudo pip3 install -U jetson-stats

sudo reboot
