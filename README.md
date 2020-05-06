# Display Google Calendar events as desktop notifications

Disclaimer: I wrote this for my own personal use. You might need to deviate from the instructions as necessary for your particular environment.

## Install Python dependencies
`python3 -m pip install requirements.txt`

## Set environment variables
`chmod +x ./pygcal_environ.sh && source ./pygcal_environ.sh`

Note: you could also try copying 'pygcal_environ.sh' to your '~/.bashrc' if you can't get it working.

## Execute setup script
`./setup_pygcal_notify.sh`

### The output of the setup script should indicate whether or not the service succeeded.
