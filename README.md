#### Fan Control for ThinkPad Laptops [GUI]

Only for Linux

###### Required Libraries

```py
pip install PySimpleGUI
```

##### Setup

1. Create new or edit existing file on - `/etc/modprobe.d/thinkpad_acpi.conf` or use this shortcut `sudo nano /etc/modprobe.d/thinkpad_acpi.conf`

2. `options thinkpad_acpi fan_control=1` paste this in and save the file

3. Reboot System

4. Run `python3 fan-control.py`


