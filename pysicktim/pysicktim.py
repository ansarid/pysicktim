import usb.core
import usb.util
import time
import unicodedata
import struct
import ctypes

################################################################
#   ERRORS

class InvalidData(Exception):
    pass

class LidarNotFound(Exception):
    pass

error_codes=[
    "Sopas_Ok",
    "Sopas_Error_METHODIN_ACCESSDENIED",
    "Sopas_Error_METHODIN_UNKNOWNINDEX",
    "Sopas_Error_VARIABLE_UNKNOWNINDEX",
    "Sopas_Error_LOCALCONDITIONFAILED",
    "Sopas_Error_INVALID_DATA",
    "Sopas_Error_UNKNOWN_ERROR",
    "Sopas_Error_BUFFER_OVERFLOW",
    "Sopas_Error_BUFFER_UNDERFLOW",
    "Sopas_Error_ERROR_UNKNOWN_TYPE",
    "Sopas_Error_VARIABLE_WRITE_ACCESSDENIED",
    "Sopas_Error_UNKNOWN_CMD_FOR_NAMESERVER",
    "Sopas_Error_UNKNOWN_COLA_COMMAND",
    "Sopas_Error_METHODIN_SERVER_BUSY",
    "Sopas_Error_FLEX_OUT_OF_BOUNDS",
    "Sopas_Error_EVENTREG_UNKNOWNINDEX",
    "Sopas_Error_COLA_A_VALUE_OVERFLOW",
    "Sopas_Error_COLA_A_INVALID_CHARACTER",
    "Sopas_Error_OSAI_NO_MESSAGE",
    "Sopas_Error_OSAI_NO_ANSWER_MESSAGE",
    "Sopas_Error_INTERNAL",
    "Sopas_Error_HubAddressCorrupted",
    "Sopas_Error_HubAddressDecoding",
    "Sopas_Error_HubAddressAddressExceeded",
    "Sopas_Error_HubAddressBlankExpected",
    "Sopas_Error_AsyncMethodsAreSuppressed",
    "Sopas_Error_ComplexArraysNotSupported"
    ]


error_descriptions = {
    "Sopas_Error_METHODIN_ACCESSDENIED": "Wrong userlevel, access to method not allowed",
    "Sopas_Error_METHODIN_UNKNOWNINDEX": "Trying to access a method with an unknown Sopas index",
    "Sopas_Error_scandatacfgVARIABLE_UNKNOWNINDEX": "Trying to access a variable with an unknown Sopas index",
    "Sopas_Error_LOCALCONDITIONFAILED": "Local condition violated, e.g. giving a value that exceeds the minimum or maximum allowed value for this variable",
    "Sopas_Error_INVALID_DATA": "Invalid data given for variable, this errorcode is deprecated (is not used anymore).",
    "Sopas_Error_UNKNOWN_ERROR": "An error with unknown reason occurred, this errorcode is deprecated.",
    "Sopas_Error_BUFFER_OVERFLOW": "The communication buffer was too small for the amount of data that should be serialised.",
    "Sopas_Error_BUFFER_UNDERFLOW": "More data was expected, the allocated buffer could not be filled.",
    "Sopas_Error_ERROR_UNKNOWN_TYPE": "The variable that shall be serialised has an unknown type. This can only happen when there are variables in the firmware of the device that do not exist in the released description of the device. This should never happen.",
    "Sopas_Error_VARIABLE_WRITE_ACCESSDENIED": "It is not allowed to write values to this variable. Probably the variable is defined as read-only.",
    "Sopas_Error_UNKNOWN_CMD_FOR_NAMESERVER": "When using names instead of indices, a command was issued that the nameserver does not understand.",
    "Sopas_Error_UNKNOWN_COLA_COMMAND": "The CoLa protocol specification does not define the given command, command is unknown.",
    "Sopas_Error_METHODIN_SERVER_BUSY": "It is not possible to issue more than one command at a time to an SRT device.",
    "Sopas_Error_FLEX_OUT_OF_BOUNDS": "An dataay was accessed over its maximum length.",
    "Sopas_Error_EVENTREG_UNKNOWNINDEX": "The event you wanted to register for does not exist, the index is unknown.",
    "Sopas_Error_COLA_A_VALUE_OVERFLOW": "The value does not fit into the value field, it is too large.",
    "Sopas_Error_COLA_A_INVALID_CHARACTER": "Character is unknown, probably not alphanumeric.",
    "Sopas_Error_OSAI_NO_MESSAGE": "Only when using SRTOS in the firmware and distributed variables this error can occur. It is an indication that no operating system message could be created. This happens when trying to GET a variable.",
    "Sopas_Error_OSAI_NO_ANSWER_MESSAGE": "This is the same as \"Sopas_Error_OSAI_NO_MESSAGE\" with the difference that it is thrown when trying to PUT a variable.",
    "Sopas_Error_INTERNAL": "Internal error in the firmware, problably a pointer to a parameter was null.",
    "Sopas_Error_HubAddressCorrupted": "The Sopas Hubaddress is either too short or too long.",
    "Sopas_Error_HubAddressDecoding": "The Sopas Hubaddress is invalid, it can not be decoded (Syntax).",
    "Sopas_Error_HubAddressAddressExceeded": "Too many hubs in the address",
    "Sopas_Error_HubAddressBlankExpected": "When parsing a HubAddress an expected blank was not found. The HubAddress is not valid.",
    "Sopas_Error_AsyncMethodsAreSuppressed": "An asynchronous method call was made although the device was built with \“AsyncMethodsSuppressed\”. This is an internal error that should never happen in a released device.",
    "Sopas_Error_ComplexArraysNotSupported": "Device was built with „ComplexArraysSuppressed“ because the compiler does not allow recursions. But now a complex dataay was found. This is an internal error that should never happen in a released device."
    }

def remove_control_characters(s):
    s = "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")
    return s

def dec_to_ascii(s):
    s = "".join(chr(x) for x in s)
    return s

def hex_to_dec(i):
    i = [ int(x,16) for x in i ]
    return i


def hex_to_meters(i):
    i = [ int(x,16)/1000 for x in i ]
    return i

def uint32(i):
    i = struct.unpack('>i', bytes.fromhex(i))[0]
    return i

def check_error(s):
    if s[0:3] == "sFA":
        error_code = error_codes[int(s[1],16)]
        error_description = error_descriptions[error_code]
        return [error_code,error_description]
    else:
        return s

def parse_str(d):
    if d == None:
        return d
    else:
        d = d.split()
        d = d[len(d)-1]
        return d

## LIDAR FUNCTIONS ##

class LiDAR:

    def connect(self, idVendor=0x19a2, idProduct=0x5001):

        lidar = usb.core.find(idVendor, idProduct)

        if lidar is None:

            raise LidarNotFound("LiDAR Device is not connected!")
            return 1

        else:

            return 0

    def read(self):

        if connected() == 0:

            arr = lidar.read(1|usb.ENDPOINT_IN,65535,timeout=100)
            arr = "".join([chr(x) for x in arr[1:-1]])
            arr = check_error(arr)
            return arr

        else:

            raise LidarNotFound("LiDAR Device is not connected!")
            return 1

    def send(self, cmd):

        if connected() == 0:

            lidar.write(2|usb.ENDPOINT_OUT,"\x02"+cmd+"\x03\0",0)

        else:

            print("LIDAR Device not found!")
            return connected()

    ######################

    def firmwarev(self):
        send('sRN FirmwareVersion')
        answer = read()
        answer = answer.split()
        answer = answer[-1]
        return answer

    def deviceident(self):
        send('sRI0')
        answer = read()
        answer = answer.split()
        answer = answer[3] + ' ' + answer[4] + ' ' + answer[5]
        return answer

    def setaccessmode(self, user="03",password="F4724744"):
        send('sMN SetAccessMode '+user+" "+password)
        answer = read()
        if answer == "sAN SetAccessMode 1":
            return 0
        else:
            return answer

    def scancfg(self):   # Read for frequency and angular resolution
        # Request Read Command
        # sRN LMPscancfg
        send('sRN LMPscancfg')
        answer = read()
        answer = answer.split()

        if len(answer) == 7:
            scan_freq = int(answer[2],16)/100
            sectors = int(answer[3],16)
            ang_res = int(answer[4],16)/10000   # Manual says uint_32?
            start_ang = int(answer[5],32)/10000
            stop_ang = int(answer[6],32)/10000
            return [scan_freq,sectors,ang_res,start_ang,stop_ang]

        else:
            return answer

    def startmeas(self):   # Start measurement
        # sMN LMCstartmeas
        send('sMN LMCstartmeas')
        answer = read()
        if answer == "sAN LMCstartmeas 0":
            return 0
        else:
            return answer
        #   Start the laser and (unless in Standby mode) the motor of the the device

    def stopmeas(self):   # Stop measurement
        # sMN LMCstopmeas
        send('sMN LMCstopmeas')
        answer = read()
        if answer == "sAN LMCstopmeas 0":
            return 0
        else:
            return answer
        #   Shut off the laser and stop the motor of the the device

    def loadfacdef(self):   # Load factory defaults
        # sMN mSCloadfacdef
        send('sMN mSCloadfacdef')
        answer = read()
        if answer == "sAN mSCloadfacdef":
            return 0
        else:
            return answer

    def loadappdef(self):    # Load application defaults
        # sMN mSCloadappdef
        send('sMN mSCloadappdef')
        answer = read()
        return answer

    def checkpassword(self,user,password):    # Check password
        # sMN CheckPassword 03 19 20 E4 C9
        send('sMN CheckPassword '+user+' '+password)
        answer = read()
        return answer
        # sAN CheckPassword  1

    def reboot(self):    # Reboot device
        # sMN mSCreboot
        send('sMN mSCreboot')#
        answer = read()
        if answer == "sAN mSCreboot":
            return 0
        else:
            return answer
        # sAN mSCreboot

    def writeall(self):    # Save parameters permanently
        # sMN mEEwriteall
        send('sMN mEEwriteall')
        answer = read()
        return answer
        # sAN mEEwriteall 1

    def run(self):    # Set to run
        # sMN Run
        send('sMN Run')
        answer = read()
        if answer == "sAN Run 1":
            return 0
        else:
            return answer
        # sAN Run 1

    #####################################################################

    #   Measurement output telegram


    # DOES NOT WORK YET
    def scandatacfg(self, channel='01 00', rem_ang=1, res=1, unit=0, enc='00 00', pos=0, name=0, comment=0, time=0, out_rate='+1'):    # Configure the data content for the scan
        # sWN LMDscandatacfg 01 00 1 1 0 00 00 0 0 0 0 +1
        # sWN LMDscandatacfg 01 00 1 1 0 00 00 0  0 0 +10
        # sWN LMDscandatacfg 02 0 0 1 0 01 0 0 0 0 0 +10
        send('sWN LMDscandatacfg '+str(channel)+' '+str(rem_ang)+' '+str(res)+' '+str(unit)+' '+str(enc)+' '+str(pos)+' '+str(name)+' '+str(comment)+' '+str(time)+' '+str(out_rate))
        answer = read()
        if answer == "sWA LMDscandatacfg":
            return 0
        else:
            return answer

        # sWA LMDscandatacfg

    def outputRange(self):    # Configure measurement angle of the scandata for output
        # sWN LMPoutputRange 1 1388 0 DBBA0
        send('sWN LMPoutputRange')
        answer = read()
        return answer
        # sWA LMPoutputRange

    def outputRange(self):    # Read for actual output range
        # sRN LMPoutputRange
        send('sRN LMPoutputRange')
        answer = read()
        return answer
        # sRA LMPoutputRange 1 1388 FFF92230 225510

    def scan(self, raw=False):    # Get LIDAR Data

        send('sRN LMDscandata')
        raw_data = read()
        data = raw_data

        if raw == False:

            self.scan.dist_start = None
            self.scan.rssi_start = None

            print(data)

            data = data.split()

            for index, item in enumerate(data):
                if "DIST" in item and self.scan.dist_start == None:
                    self.scan.dist_start = index

                if "RSSI" in item:
                    self.scan.rssi_start = index

            self.scan.telegram_len = len(data)
            self.scan.cmd_type =         data[0]
            self.scan.cmd =              data[1]
            self.scan.version =      int(data[2],16)
            self.scan.device_num =   int(data[3],16)
            self.scan.serial_num =   int(data[4],16)
            self.scan.device_stat =  int(data[6],8)
            self.scan.telegram_cnt = int(data[7],16)
            self.scan.scan_cnt =     int(data[8],16)
            self.scan.uptime =       int(data[9],32)
            self.scan.trans_time =   int(data[10],32)
            # self.scan.input_stat =   int(str(data[11],data[12]),32)    # Takes both bytes into account
            self.scan.input_stat =   int(data[12],32)
            # self.scan.output_stat =  int(str(data[13],data[14]),8)     # Takes both bytes into account
            self.scan.output_stat =  int(data[14],8)
            self.scan.layer_ang =    int(data[15],16)
            self.scan.scan_freq =    int(data[16],32)/100
            self.scan.meas_freq =    int(data[17],16)/100   # Math may not be right
            self.scan.enc_amount =   int(data[18],16)

            self.scan.num_16bit_chan = int(data[19],16)

            if self.scan.dist_start != None:

                self.scan.dist_label = data[20]
                self.scan.dist_scale_fact = int(data[self.scan.dist_start+1],16)
                self.scan.dist_scale_fact_offset = int(data[self.scan.dist_start+2],16)
                self.scan.dist_start_ang = uint32(data[self.scan.dist_start+3])/10000
                self.scan.dist_angle_res = int(data[self.scan.dist_start+4],16)/10000
                self.scan.dist_data_amnt = int(data[self.scan.dist_start+5],16)
                self.scan.dist_end = (self.scan.dist_start+6) + self.scan.dist_data_amnt
                self.scan.distances = hex_to_meters(data[self.scan.dist_start+6:self.scan.dist_end])
                self.scan.raw_distances = " ".join(data[self.scan.dist_start+6:self.scan.dist_end])

            else:

                self.scan.dist_label = None
                self.scan.dist_scale_fact = None
                self.scan.dist_scale_fact_offset = None
                self.scan.dist_start_ang = None
                self.scan.dist_angle_res = None
                self.scan.dist_data_amnt = None
                self.scan.dist_end = None
                self.scan.distances = None
                self.scan.raw_distances = None

            if self.scan.rssi_start != None:

                self.scan.rssi_label = data[20]
                self.scan.rssi_scale_fact = int(data[self.scan.rssi_start+1],16)
                self.scan.rssi_scale_fact_offset = int(data[self.scan.rssi_start+2],16)
                self.scan.rssi_start_ang = uint32(data[self.scan.rssi_start+3])/10000
                self.scan.rssi_angle_res = int(data[self.scan.rssi_start+4],16)/10000
                self.scan.rssi_data_amnt = int(data[self.scan.rssi_start+5],16)
                self.scan.rssi_end = (self.scan.rssi_start+6) + self.scan.rssi_data_amnt
                self.scan.rssi = data[self.scan.rssi_start+6:self.scan.rssi_end]

            else:

                self.scan.rssi_label = None
                self.scan.rssi_scale_fact = None
                self.scan.rssi_scale_fact_offset = None
                self.scan.rssi_start_ang = None
                self.scan.rssi_angle_res = None
                self.scan.rssi_data_amnt = None
                self.scan.rssi_end = None
                self.scan.rssi = None

            return raw_data

    # LMDscandata - reserved values PAGE 80

    #####################################################################
    #   Filter

    def particle(self):    # Set particle filter
        # sWN LFPparticle 1 +500
        send('sWN LFPparticle')
        answer = read()
        return answer
        # sWA LFPparticle

    def meanfilter(self, status_code=0,number_of_scans="+10"):    # Set mean filter
        # sWN LFPmeanfilter 1 +10 0
        send('sWN LFPmeanfilter '+status_code+' '+number_of_scans+' 0')
        answer = read()
        return answer
        # sWA LFPmeanfilter


    #####################################################################
    #   Outputs



    def outputstate(self):    # Read state of the outputs
        # sRN LIDoutputstate
        send('sRN LIDoutputstate')

    def eventoutputstate(self, state):    # Send outputstate by event
        send('sEN LIDoutputstate '+str(state))
        answer = read()
        return answer

    def setoutput(self):    # Set output state
        # sMN mDOSetOutput 1 1
        send('sMN mDOSetOutput')
        answer = read()
        return answer
        # sAN mDOSetOutput 1
    #####################################################################
    #   Inputs

    def debtim(self):    # Set debouncing time for input x
        # sWN DI3DebTim +10
        send('sWN DI3DebTim')
        answer = read()
        return answer
        # sWA DI3DebTim

    def deviceident(self):    # Read device ident
        # sRN DeviceIdent
        send('sRN DeviceIdent')
        answer = read()
        answer = answer.split()
        answer = answer[3] + ' ' + answer[4] + ' ' + answer[5]
        return answer
        # sRA DeviceIdent 10 LMS10x_FieldEval 10 V1.36-21.10.2010

    def devicestate(self):    # Read device state
        # sRN SCdevicestate
        send('sRN SCdevicestate')
        answer = read()
        return answer
        # sRA SCdevicestate 0

    def ornr(self):    # Read device information
        # sRN DIornr
        send('sRN DIornr')
        answer = read()
        return answer
        # sRA DIornr 1071419

    def devicetype(self):    # Device type
        # sRN DItype
        send('sRN DItype')
        answer = read()
        return answer
        # sRA DItype E TIM561-2050101

    def oprh(self):    # Read operating hours
        # sRN ODoprh
        send('sRN ODoprh')
        answer = read()
        return answer
        # sRA ODoprh 2DC8B

    def pwrc(self):    # Read power on counter
        # sRN ODpwrc
        send('sRN ODpwrc')
        answer = read()
        return answer
        # sRA ODpwrc 752D

    def setLocationName(self, name):    # Set device name
        # sWN LocationName +13 OutdoorDevice
        name = " " + name
        string = 'sWN LocationName +'+str(len(name)-1)+name
        send(string)
        answer = read()
        return answer
        # sWA LocationName

    def readLocationName(self):    # Read for device name
        # sRN LocationName
        send('sRN LocationName')
        answer = read()
        answer = parse_str(answer)
        return answer
        # sRA LocationName D OutdoorDevice

    def rstoutpcnt(self):    # Reset output counter
        # sMN LIDrstoutpcnt
        send('sMN LIDrstoutpcnt')
        answer = read()
    #    answer = parse_str(answer)
        return answer
        # sAN LIDrstoutpcnt 0
