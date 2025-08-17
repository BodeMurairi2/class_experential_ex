#!/usr/bin/env bash

# Enable the firewall
sudo ufw enable

# Deny incoming traffic to port 53
sudo ufw deny in proto tcp to any port 53
sudo ufw deny in proto udp to any port 53

# Deny outgoing traffic to port 53
sudo ufw deny out proto tcp to any port 53
sudo ufw deny out proto udp to any port 53
#.........................................................
sudo ufw default deny outgoing && sudo ufw allow 22/tcp
sudo ufw default deny incoming && sudo ufw allow 22/tcp
