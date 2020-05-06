#!/bin/bash

## copy service file to systemd user folder:
cp pygcal-notify.service ~/.config/systemd/user/

## add executable permissions
chmod +x ./pygcal_environ.sh
chmod +x ~/.config/systemd/user/pygcal-notify.service

## enable, start service
systemctl enable --user ~/.config/systemd/user/pygcal-notify.service
systemctl --user start pygcal-notify.service

## print service status
systemctl --user status pygcal-notify.service
