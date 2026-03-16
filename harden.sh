#!/bin/bash

# Secure local Vault
mkdir -p ~/Vault
chmod 700 ~/Vault

# Fix /etc/shadow (requires sudo)
sudo chmod 640 /etc/shadow
sudo chown root:shadow /etc/shadow
