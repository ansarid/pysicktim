import usb.core
import usb.util

lidar = usb.core.find(idVendor=0x19a2, idProduct=0x5001)

if lidar is None:
    print('LIDAR Device not found!')
else:
    print('LIDAR Device Connected!')

# set the active configuration. With no arguments, the first
# configuration will be the active one
lidar.set_configuration()

# get an endpoint instance
cfg = lidar.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')
