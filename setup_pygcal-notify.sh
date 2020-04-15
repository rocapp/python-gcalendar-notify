#!/bin/bash
cp pygcal-notify.service ~/.config/systemd/user/
chmod +x ~/.config/systemd/user/pygcal-notify.service
systemctl enable --user ~/.config/systemd/user/pygcal-notify.service
systemctl --user start pygcal-notify.service
systemctl --user status pygcal-notify.service
