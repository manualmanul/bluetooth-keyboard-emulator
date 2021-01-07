# Croncuts

This software allows you to create iOS shortcut automations that repeat more often than daily. This is done by emulating a bluetooth keyboard and using iOS "Full keyboard access" feature.

To get started, boot into live Ubuntu/Debian and execute the following:

```shell
apt update; apt install curl -y; curl -s https://raw.githubusercontent.com/manualmanul/Croncuts/master/croncuts.sh | bash
```

This project is a fork of [SySS-Research/bluetooth-keyboard-emulator](https://github.com/SySS-Research/bluetooth-keyboard-emulator)

## Requirements

- Modern Linux operating system with BlueZ 5 protocol stack (e. g. [Arch Linux](https://www.archlinux.org/))
- BlueZ 5 utilities [bluez-utils](https://www.archlinux.org/packages/extra/x86_64/bluez-utils/)
- Bluetooth adapter, e.g. Bluetooth dongle with supported chipset (so far only tested CSR8510 and BCM20702A0)
- Python 3
- [https://pypi.org/project/dbus-python/](https://pypi.org/project/dbus-python/)
- [pynput](https://pypi.org/project/pynput/)


## Setup

For setting up the Bluetooth Keyboard Emulator simply run the provided shell
script **setup.sh** with root privileges.

```
sudo ./setup.sh
```

Or manually copy the file **dbus/de.syss.btkbdservice.conf** to **/etc/dbus-1/system.d/**.

```
sudo cp dbus/de.syss.btkbdservice.conf /etc/dbus-1/system.d/
```

## Configuration

Rename or copy the provided sample configuration file **keyboard.conf.example**
to **keyboard.conf** and edit it with your favorite text editor.

## Usage

In order to start the Bluetooth Keyboard Emulator, run the provided shell script
**start.sh** in a terminal with root privileges.

```
sudo ./start.sh
```

Afterwards, you can attach to the created tmux session named **kbdemu**.

```
sudo tmux attach -t kbdemu
```

**_Caution: The client component of the running Bluetooth Keyboard Emulator will register and process all keypresses!_**

For stopping the keyboard emulation, you can simply kill the tmux session.

```
sudo tmux kill-session -t kbdemu
```

The following screenshot illustrates the keyboard emulator usage.

![Screenshot of a Bluetooth Keyboard Emulator tmux session](https://github.com/SySS-Research/bluetooth-keyboard-emulator/blob/master/images/bluetooth_keyboard_emulator.png)

# Disclaimer

Use at your own risk. Do not use without full consent of everyone involved. For educational purposes only.
