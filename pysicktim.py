import usb.core
import usb.util

'''

    Command basics
    ┌──────────────────┬────────────────┬────────────────────────────────┬────────────────────────────────┐
    │   Description    │ Value ASCII    │ Value Hex                      │ Value Binary                   │
    ├──────────────────┼────────────────┼────────────────────────────────┼────────────────────────────────┤
    │   Start of text  │ <STX>          │ 02                             │ 02 02 02 02 + given length     │
    ├──────────────────┼────────────────┼────────────────────────────────┼────────────────────────────────┤
    │   End of text    │ <ETX>          │ 03                             │ Calculated checksum            │
    ├──────────────────┼────────────────┼────────────────────────────────┴────────────────────────────────┤
    │   Read           │ sRN            │                             73 52 4E                            │
    ├──────────────────┼────────────────┼─────────────────────────────────────────────────────────────────┤
    │   Write          │ sWN            │                             73 57 4E                            │
    ├──────────────────┼────────────────┼─────────────────────────────────────────────────────────────────┤
    │   Method         │ sMN            │                             73 4D 4E                            │
    ├──────────────────┼────────────────┼─────────────────────────────────────────────────────────────────┤
    │   Event          │ sEN            │                             73 45 4E                            │
    ├──────────────────┼────────────────┼─────────────────────────────────────────────────────────────────┤
    │   Answer         │ sRA            │                             73 52 41                            │
    │                  │ sWA            │                             73 57 41                            │
    │                  │ sAN            │                             73 41 4E                            │
    │                  │ sEA            │                             73 45 41                            │
    │                  │ sSN            │                             73 53 4E                            │
    ├──────────────────┼────────────────┼────────────────────────────────┬────────────────────────────────┤
    │   Space          │ {SPC}          │ 20                             │ 20                             │
    └──────────────────┴────────────────┴────────────────────────────────┴────────────────────────────────┘

    If values are divided into two parts (e.g. measurement data), they are documented
    according to LSB 0 (e.g. 00 07), output however is according to MSB (e.g. 07 00).

'''

lidar = usb.core.find(idVendor=0x19a2, idProduct=0x5001)

if lidar is None:
    print('LIDAR Device not found!')
else:
    print('LIDAR Device Connected!')

lidar.set_configuration()

############################################
#   Basic Settings

def send_cmd(cmd):
        lidar.write(2|usb.ENDPOINT_OUT,"\x02"+cmd+"\x03\0",0)
        arr = lidar.read(1|usb.ENDPOINT_IN,65535,timeout=100)
        return "".join(chr(x) for x in arr)

def LMPscancfg():   # Read for frequency and angular resolution
    # Request Read Command
    # sRN LMPscancfg
    data = send_cmd('sRN LMPscancfg').split()
    return data

def LMCstartmeas():   # Start measurement
    # sMN LMCstartmeas
    data = send_cmd('sMN LMCstartmeas').split()
    return data
    #   Start the laser and (unless in Standby mode) the motor of the the device

def LMCstopmeas():   # Stop measurement
    # sMN LMCstopmeas
    data = send_cmd('sMN LMCstopmeas').split()
    return data

def mSCloadfacdef():   # Load factory defaults
    # sMN mSCloadfacdef
    data = send_cmd('sMN mSCloadfacdef').split()
    return data
#   Shut off the laser and stop the motor of the the device

# def LMPscancfg():    # Load factory defaults
    # sAN mSCloadfacdef
#     data = send_cmd('sAN mSCloadfacdef').split()
#     return data

def mSCloadappdef():    # Load application defaults
    # sMN mSCloadappdef
    data = send_cmd('sMN mSCloadappdef').split()
    return data

# def LMPscancfg():    # Load factory defaults
    # sAN mSCloadappdef
#     data = send_cmd('sAN mSCloadappdef').split()
#     return data




def CheckPassword():    # Check password
    # sMN CheckPassword 03 19 20 E4 C9
    data = send_cmd('sMN CheckPassword').split()
    return data
    # sAN CheckPassword  1




def mSCreboot():    # Reboot device
    # sMN mSCreboot
    data = send_cmd('sMN mSCreboot').split()
    return data
    # sAN mSCreboot





def sMN mEEwriteall():    # Save parameters permanently
    # sMN mEEwriteall
    data = send_cmd('sMN mEEwriteall').split()
    return data
    # sAN mEEwriteall 1



def Run():    # Set to run
    # sMN Run
    data = send_cmd('sMN Run').split()
    return data
    # sAN Run 1




#####################################################################
#   Measurement output telegram




def LMDscandatacfg():    # Configure the data content for the scan
    # sWN LMDscandatacfg 01 00 1 1 0 00 00 0 0 0 0 +1
    # sWN LMDscandatacfg 01 00 1 1 0 00 00 0  0 0 +10
    # sWN LMDscandatacfg 02 0 0 1 0 01 0 0 0 0 0 +10
    data = send_cmd('sWN LMDscandatacfg').split()
    return data
    # sWA LMDscandatacfg



def LMPoutputRange():    # Configure measurement angle of the scandata for output
    # sWN LMPoutputRange 1 1388 0 DBBA0
    data = send_cmd('sWN LMPoutputRange').split()
    return data
    # sWA LMPoutputRange




def LMPoutputRange():    # Read for actual output range
    # sRN LMPoutputRange
    data = send_cmd('sRN LMPoutputRange').split()
    return data
    # sRA LMPoutputRange 1 1388 FFF92230 225510




def LMDscandata(cont=False,cont_mode=0):    # Get LIDAR Data
    if cont == "True":
        data = send_cmd('sEN LMDscandata', cont_mode).split()  # Send Telegrams Continuously
    else:
        data = send_cmd('sRN LMDscandata').split()  # Request single telegram
    return data
# LMDscandata - reserved values PAGE 80




#####################################################################
#   Filter



def LFPparticle():    # Set particle filter
    # sWN LFPparticle 1 +500
    data = send_cmd('sWN LFPparticle').split()
    return data
    # sWA LFPparticle




def LFPmeanfilter():    # Set mean filter
    # sWN LFPmeanfilter 1 +10 0
    data = send_cmd('sWN LFPmeanfilter').split()
    return data
    # sWA LFPmeanfilter




#####################################################################
#   Outputs




def LIDoutputstate():    # Read state of the outputs
    # sRN LIDoutputstate
    data = send_cmd('sRN LIDoutputstate').split()
    return data


def LIDoutputstate():    # Send outputstate by event
    # sEN LIDoutputstate 1
    data = send_cmd('sEN LIDoutputstate').split()
    return data





def mDOSetOutput():    # Set output state
    # sMN mDOSetOutput 1 1
    data = send_cmd('sMN mDOSetOutput').split()
    return data
    # sAN mDOSetOutput 1


#####################################################################
#   Inputs


def DI3DebTim():    # Set debouncing time for input x
    # sWN DI3DebTim +10
    data = send_cmd('sWN DI3DebTim').split()
    return data
    # sWA DI3DebTim





def DeviceIdent():    # Read device ident
    # sRN DeviceIdent
    data = send_cmd('sRN DeviceIdent').split()
    return data
    # sRA DeviceIdent 10 LMS10x_FieldEval 10 V1.36-21.10.2010



def SCdevicestate():    # Read device state
    # sRN SCdevicestate
    data = send_cmd('sRN SCdevicestate').split()
    return data
    # sRA SCdevicestate 0




def DIornr():    # Read device information
    # sRN DIornr
    data = send_cmd('sRN DIornr').split()
    return data
    # sRA DIornr 1071419




def DItype():    # Device type
    # sRN DItype
    data = send_cmd('sRN DItype').split()
    return data
    # sRA DItype E TIM561-2050101




def ODoprh():    # Read operating hours
    # sRN ODoprh
    data = send_cmd('sRN ODoprh').split()
    return data
    # sRA ODoprh 2DC8B




def ODpwrc():    # Read power on counter
    # sRN ODpwrc
    data = send_cmd('sRN ODpwrc').split()
    return data
    # sRA ODpwrc 752D




def LocationName():    # Set device name
    # sWN LocationName +13 OutdoorDevice
    data = send_cmd('sWN LocationName').split()
    return data
    # sWA LocationName




def LocationName():    # Read for device name
    # sRN LocationName
    data = send_cmd('sRN LocationName').split()
    return data
    # sRA LocationName D OutdoorDevice




def LIDrstoutpcnt():    # Reset output counter
    # sMN LIDrstoutpcnt
    data = send_cmd('sMN LIDrstoutpcnt').split()
    return data
    # sAN LIDrstoutpcnt 0

while 1:
    data = LMDscandata()
    print(data)
