#!/usr/bin/env python3

"""Program which detects USB serial ports.

This program will search for a USB serial port using a search criteria.
In its simplest form, you can use the -l (--list) option to list all of
the detected serial ports.

You can also add the following filters:

--vid 2341      Will only match devices with a Vendor ID of 2341.
--pid 0001      Will only match devices with a Product ID of 0001
--vendor Micro  Will only match devices whose vendor name starts with Micro
--seral  00123  Will only match devices whose serial number starts with 00123

If you use -l or --list then detailed information about all of the matches
will be printed. If you don't use -l (or --list) then only the name of
the device will be printed (i.e. /dev/ttyACM0). This is useful in scripts
where you want to pass the name of the serial port into a utiity to open.
"""

import sys
import argparse
import serial
import serial.tools.list_ports

def is_usb_serial(port, args):
    """Checks device to see if its a USB Serial device.

    The caller already filters on the subsystem being 'tty'.

    If serial_num or vendor is provided, then it will further check to
    see if the serial number and vendor of the device also matches.
    """
    if port.vid is None:
        return False
    if not args.vid is None:
        if port.vid != args.vid:
            return False
    if not args.pid is None:
        if port.pid != args.pid:
            return False
    if not args.vendor is None:
        if not port.manufacturer.startswith(args.vendor):
            return False
    if not args.serial is None:
        if not port.serial_number.startswith(args.serial):
            return False
    if not args.intf is None:
        if port.interface is None or not args.intf in port.interface:
            return False
    return True


def extra_info(port):
    """Collects the serial nunber and manufacturer into a string, if
       the fields are available."""
    extra_items = []
    if port.manufacturer:
        extra_items.append("vendor '{}'".format(port.manufacturer))
    if port.serial_number:
        extra_items.append("serial '{}'".format(port.serial_number))
    if port.interface:
        extra_items.append("intf '{}'".format(port.interface))
    if extra_items:
        return ' with ' + ' '.join(extra_items)
    return ''


def main():
    """The main program."""
    parser = argparse.ArgumentParser(
        prog="find-port.py",
        usage="%(prog)s [options] [command]",
        description="Find the /dev/tty port for a USB Serial devices",
    )
    parser.add_argument(
        "-l", "--list",
        dest="list",
        action="store_true",
        help="List USB Serial devices currently connected"
    )
    parser.add_argument(
        "-s", "--serial",
        dest="serial",
        help="Only show devices with the indicated serial number",
        default=None,
    )
    parser.add_argument(
        "-n", "--vendor",
        dest="vendor",
        help="Only show devices with the indicated vendor name",
        default=None
    )
    parser.add_argument(
        "--pid",
        dest="pid",
        action="store",
        help="Only show device with indicated PID",
        default=None
    )
    parser.add_argument(
        "-v", "--verbose",
        dest="verbose",
        action="store_true",
        help="Turn on verbose messages",
        default=False
    )
    parser.add_argument(
        "--vid",
        dest="vid",
        action="store",
        help="Only show device with indicated VID",
        default=None
    )
    parser.add_argument(
        '-i', '--intf',
        dest='intf',
        action='store',
        help='Shows devices which conatin the indicated interface string',
        default=None
    )
    args = parser.parse_args(sys.argv[1:])

    if args.verbose:
        print('pyserial version = {}'.format(serial.__version__))
        print('   vid =', args.vid)
        print('   pid =', args.pid)
        print('serial =', args.serial)
        print('vendor =', args.vendor)

    if args.list:
        detected = False
        for port in serial.tools.list_ports.comports():
            if is_usb_serial(port, args):
                print('USB Serial Device {:04x}:{:04x}{} found @{}\r'.format(
                    port.vid, port.pid,
                    extra_info(port), port.device))
                detected = True
        if not detected:
            print('No USB Serial devices detected.\r')
        return

    for port in serial.tools.list_ports.comports():
        if is_usb_serial(port, args):
            print(port.device)
            return
    sys.exit(1)


main()
