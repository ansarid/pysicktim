# PySICKTiM - A Python Library for the SICK TiM5xx

Introduction
------

This is a python library made to interact with the SICK TiM561 LiDAR sensor over the USB connection. This library was created to help developers who are using python to implement the TiM5xx LiDAR easily into their projects using python.

 The functions of this library includes:
 * Reading Settings and Data
 * Configuring Settings
 * Error Handling. 

The functions in this library are based off the [TiM5xx Series LiDAR](https://cdn.sick.com/media/docs/7/27/927/Technical_information_Telegram_Listing_Ranging_sensors_LMS1xx_LMS5xx_TiM5xx_MRS1000_MRS6000_NAV310_LD_OEM15xx_LD_LRS36xx_LMS4000_en_IM0045927.PDF) telegram documentation.

Prerequisites
------
    pyusb
pip3 install pyusb

Installation
------

from [PyPI](https://pypi.org/project/pysicktim/)

    pip3 install pysicktim

from source:

    git clone https://github.com/ansarid/pysicktim
    cd pysicktim
    pip3 install -r requirements.txt
    python3 setup.py install

## Allow non-root access:
```
sudo cp ./udev /etc/udev/rules.d/sick-tim5xx.rules
sudo reboot
```

Tutorial
------
