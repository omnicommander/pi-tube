# OMNICOMMANDER Digital Signage

## Installation

1. Using the [Raspberry Pi Imager](https://www.raspberrypi.org/software/), install Raspberry Pi OS onto an SD card.

2. Insert the SD card into the Pi, then follow the installation instructions upon boot.

3. Open a terminal, and clone this repository using `git clone https://github.com/omnicommander/oc-digitalsignage`.

4. Run the install script with `sudo /home/pi/OC-DigitalSignage/install`, case sensitive.

5. Change the `pi_id` in config.sh and config.yaml using nano (or whichever editor you prefer).

6. Reboot and enjoy!

## NOTE
Because the updated scripts are still in development, any changes made to a config must be made in both config.sh and config.yaml

Also, push.py is not currently working