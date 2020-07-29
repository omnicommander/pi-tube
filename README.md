# Omnicommander Digital Signage AWS Branch
This is an extension of the original project, with the goal of transferring our video hosting from Youtube to AWS.

Most of the software is written in shell (bash), but is being translated into python for longevity.

### NOTE

The mouse and most gui elements *WILL* be hidden by this software, so in order to edit anything in the device, you should either use the terminal emulator (launched with `ctrl-alt-t`) or ssh (`ssh pi@hostname`).

You should not need to run the install script more than once.

Your user's name MUST be "pi" in order to work properly (currently).

# Installation
To start installation use

`$ cd OC-DigitalSignage`

and

`$ sudo ./install`

# Configuration
You can edit the config.sh to change the PI_ID and paths to various folders.

In order to easily change the WiFi settings, run the setup script by going to your home folder and running

`sudo ./config`

It will prompt you to enter your WiFi name and password.

# Troubleshooting
One of the most common problems when running this script is incomplete dependencies.
Run the install script again in order to install any missing software.

# TODO
* Auto update
* Uninstaller
* Command line tools
