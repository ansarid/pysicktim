import usb.core
import usb.util
import time
import unicodedata
import struct
import ctypes

global demo
global telegram

demo = False

if demo != True:

    lidar = usb.core.find(idVendor=0x19a2, idProduct=0x5001)

    if lidar is None:

        print('LIDAR Device not found!')
#        exit()

def demo_data(demo_mode=True,file=None):

    demo = demo_mode

    telegram = ''

    if file != None:

        try:

            file = open(file, 'r')
            telegram =file.read()

        except FileNotFoundError:

            print("Error: Demo data file path not valid!")
            pass

    if file == None:

        telegram = "sRA LMDscandata 1 1 1078AAA 0 0 BFD BFF CFACE0D CFAE156 0 0 1 0 0 5DC A2 0 1 DIST1 3F800000 00000000 FFF92230 D05 32B 24B 257 260 277 287 28D 296 29A 2A2 2A1 28E 280 284 28C 287 280 292 29A 2A1 2A0 29C 29D 29C 297 295 294 284 284 276 274 278 277 279 28C 28B 28A 28F 29A 287 279 280 285 284 27F 27F 284 278 27A 275 273 272 25B 22C 221 21C 218 21A 212 216 21D 23E 25D 25F 25B 24E 254 252 256 24B 243 22D 21A 20F 211 213 20F 216 224 234 241 242 241 242 23B 241 23A 230 235 22B 21F 218 206 1EE 1B8 186 17B 17A 173 173 171 171 16A 16B 16D 16B 16B 168 16D 168 168 167 165 166 165 168 167 165 161 162 163 15F 164 15F 15E 157 15E 158 158 154 153 156 154 151 156 15C 18C 1D7 1ED 1F8 20B 208 20D 214 215 21C 21C 21B 225 224 22A 224 228 229 229 22A 22D 225 22A 220 225 229 225 226 22C 228 22C 22B 229 22A 21A 219 20E 204 205 1FD 204 204 203 200 205 205 205 205 205 205 206 20B 207 20C 20E 212 226 27A 2B0 2AE 2AC 2B0 2B7 2B5 2C3 2CE 2CE 2CC 2DA 2D9 2DF 2E1 2E3 2E2 2E3 2E8 2EC 2EC 2F3 2F5 2FA 2FA 2FA 2FD 306 305 301 305 310 30C 313 318 31D 318 31B 324 322 31D 32A 32B 32F 331 334 336 339 335 339 340 345 34A 34A 34A 31C 270 243 23D 246 247 24C 24B 245 241 249 24D 24E 249 242 254 24E 254 258 250 254 25C 257 250 252 255 255 255 256 258 25C 25B 25A 260 25B 25E 25C 262 260 263 264 266 268 26A 26A 26B 26C 26D 270 26F 26E 271 273 272 272 278 277 27C 27A 27B 281 280 27F 282 283 280 283 288 288 288 28D 28B 290 291 293 293 297 299 29B 29B 29D 2A4 2A1 2A6 2A8 2A8 2A9 2AD 2AF 2B2 2B2 2B8 2B5 2BA 2BC 2BE 2C3 2C6 2C7 2C9 2C8 2D0 2D3 2D1 2D5 2D9 2DB 2DB 2E3 2E0 2E5 2EC 2ED 2EE 2F3 2F4 2FD 2FD 300 301 2FE 2F9 2EE 674 655 65F 654 667 673 67E 680 688 69C 6B4 0 393 38B 0 65A 65E 66A 674 674 67D 686 689 66E 669 6AC 79B 7FE 813 80E 817 80F 810 80F 81B 811 7F7 7CA 7D3 7F8 7D2 7E3 7FB 6A8 4BB 412 4D0 583 58B 592 5F4 6E2 6F0 698 6B4 6BA 67A 643 625 635 674 6B1 6B3 6A9 67D 6A3 6B1 694 675 684 6AD 6CD 669 66B 7FC 859 863 862 865 85C 700 6D0 6E5 6E2 70B 716 717 714 705 703 6DD 2 2 62B 5F5 5E9 5EE 5F0 5F7 D22 0 0 0 0 0 0 644 640 639 63A 639 646 643 651 657 65A 693 7A7 7CA 7DB 7E2 7EA 7EF 7FD 807 811 815 824 82C 834 83D 84A 852 860 86B 876 879 889 89A 8A3 8B0 8BE 8CC 8D9 8ED 8F4 8F1 8EA 900 916 926 926 92E 936 93C 943 94E 94D 959 962 961 96F 972 985 98A 98C 993 99B 9A6 9B1 9BA 9BF 9C6 9D8 9D9 9EA 9F2 9FC 9FB 9E5 9CA 9C7 9CB 9B7 9AD 9A6 9A7 9B5 9C7 9DA 9EC 9FF A14 A1F A37 0 0 0 0 0 0 0 1139 0 0 0 EB9 ED3 EF4 F1B F3C F5A 8BA 8B3 8BD FCB 1007 1055 1076 1097 1060 1044 1049 104E 105B 1069 1068 1075 1076 1086 108F 10AE 3E4 374 2F6 306 2F7 2FE 301 2FA 2F0 2F3 308 30A 309 308 314 321 37C 3BF 3BC 3BD 3C0 3C1 3BA 3C3 3BB 3C2 3C3 3C1 3C7 3C0 3C2 3BC 3BF 3C5 3CB 3C3 3C9 3C5 3C7 3CD 3BE 3C1 3B1 3B9 3BC 3C0 3BE 3C3 3C7 3CC 3CE 3DE 3DF 3DB 3E3 3EA 3F5 401 400 40B 424 43E 44E 2056 ED3 EC2 EBD EBA EBA EBD EBA EB8 EB5 EB8 EBA 805 7B8 7A1 794 78B 780 774 76B 767 761 762 763 779 7B0 7F0 7FA 803 812 81B 81D 819 8AE 86C 117A 1184 1184 118E 118E 1197 1195 1193 1191 1197 119B 11AB 11AD 11A3 11A5 11B3 11C7 11F5 234E 11FE 602 600 5FF 5FF 60A 0 0 0 0 0 0 0 0 0 7F8 7AA D2C D23 D2B 0 0 0 1348 1327 1310 1308 B6F B8D BD0 CCA CEC CF1 D0A 847 85E 83F 82B 818 807 7F9 801 80A 2 870 853 83B 81D 814 7E2 7C3 7BC 7BF 380 391 390 375 37A 37C A19 0 2 2 2 2DA 33A 34A 34E 346 982 AC 86 29B 295 9B 7B 73 72 77 72 70 73 71 73 74 77 72 71 71 77 79 79 0 0 1 7 Daniyal 0 0 0"

    if type(telegram) != list:
        telegram = remove_control_characters(telegram)
        telegram = telegram.split(' ')

    return telegram

################################################################
#   ERRORS

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

############################################
#   Basic Settings

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

def read():
    arr = lidar.read(1|usb.ENDPOINT_IN,65535,timeout=100)
    arr = "".join([chr(x) for x in arr[1:-1]])
    arr = check_error(arr)
    return arr

def send(cmd):
    lidar.write(2|usb.ENDPOINT_OUT,"\x02"+cmd+"\x03\0",0)
######################

def firmwarev():
    send('sRN FirmwareVersion')
    answer = read()
    answer = answer.split()
    answer = answer[-1]
    return answer

def deviceident():
    send('sRI0')
    answer = read()
    answer = answer.split()
    answer = answer[3] + ' ' + answer[4] + ' ' + answer[5]
    return answer

def setaccessmode(user="03",password="F4724744"):
    send('sMN SetAccessMode '+user+" "+password)
    answer = read()
    if answer == "sAN SetAccessMode 1":
        return 0
    else:
        return answer

def scancfg():   # Read for frequency and angular resolution
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

def startmeas():   # Start measurement
    # sMN LMCstartmeas
    send('sMN LMCstartmeas')
    answer = read()
    if answer == "sAN LMCstartmeas 0":
        return 0
    else:
        return answer
    #   Start the laser and (unless in Standby mode) the motor of the the device

def stopmeas():   # Stop measurement
    # sMN LMCstopmeas
    send('sMN LMCstopmeas')
    answer = read()
    if answer == "sAN LMCstopmeas 0":
        return 0
    else:
        return answer
    #   Shut off the laser and stop the motor of the the device

def loadfacdef():   # Load factory defaults
    # sMN mSCloadfacdef
    send('sMN mSCloadfacdef')
    answer = read()
    if answer == "sAN mSCloadfacdef":
        return 0
    else:
        return answer

def loadappdef():    # Load application defaults
    # sMN mSCloadappdef
    send('sMN mSCloadappdef')
    answer = read()
    return answer

def checkpassword(user,password):    # Check password
    # sMN CheckPassword 03 19 20 E4 C9
    send('sMN CheckPassword '+user+' '+password)
    answer = read()
    return answer
    # sAN CheckPassword  1

def reboot():    # Reboot device
    # sMN mSCreboot
    send('sMN mSCreboot')#
    answer = read()
    if answer == "sAN mSCreboot":
        return 0
    else:
        return answer
    # sAN mSCreboot

def writeall():    # Save parameters permanently
    # sMN mEEwriteall
    send('sMN mEEwriteall')
    answer = read()
    return answer
    # sAN mEEwriteall 1

def run():    # Set to run
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


#DOES NOT WORK YET
def scandatacfg(channel='01 00', rem_ang=1, res=1, unit=0, enc='00 00', pos=0, name=0, comment=0, time=0, out_rate='+1'):    # Configure the data content for the scan
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

def outputRange():    # Configure measurement angle of the scandata for output
    # sWN LMPoutputRange 1 1388 0 DBBA0
    send('sWN LMPoutputRange')
    answer = read()
    return answer
    # sWA LMPoutputRange

def outputRange():    # Read for actual output range
    # sRN LMPoutputRange
    send('sRN LMPoutputRange')
    answer = read()
    return answer
    # sRA LMPoutputRange 1 1388 FFF92230 225510

def scan(raw=False):    # Get LIDAR Data

    if demo == False:

        send('sRN LMDscandata')
        raw_data = read()
        data = raw_data

    elif demo == True:

        raw_data = demo_data()
        data = raw_data

    if raw == False:

        scan.dist_start = None
        scan.rssi_start = None

        data = data.split()

        for index, item in enumerate(data):
            if "DIST" in item and scan.dist_start == None:
                scan.dist_start = index

            if "RSSI" in item:
                scan.rssi_start = index

        scan.telegram_len = len(data)
        scan.cmd_type =         data[0]
        scan.cmd =              data[1]
        scan.version =      int(data[2],16)
        scan.device_num =   int(data[3],16)
        scan.serial_num =   int(data[4],16)
        scan.device_stat =  int(data[6],8)
        scan.telegram_cnt = int(data[7],16)
        scan.scan_cnt =     int(data[8],16)
        scan.uptime =       int(data[9],32)
        scan.trans_time =   int(data[10],32)
        # scan.input_stat =   int(str(data[11],data[12]),32)    # Takes both bytes into account
        scan.input_stat =   int(data[12],32)
        # scan.output_stat =  int(str(data[13],data[14]),8)     # Takes both bytes into account
        scan.output_stat =  int(data[14],8)
        scan.layer_ang =    int(data[15],16)
        scan.scan_freq =    int(data[16],32)/100
        scan.meas_freq =    int(data[17],16)/100   # Math may not be right
        scan.enc_amount =   int(data[18],16)

        scan.num_16bit_chan = int(data[19],16)

        if scan.dist_start != None:

            scan.dist_label = data[20]
            scan.dist_scale_fact = int(data[scan.dist_start+1],16)
            scan.dist_scale_fact_offset = int(data[scan.dist_start+2],16)
            scan.dist_start_ang = uint32(data[scan.dist_start+3])/10000
            scan.dist_angle_res = int(data[scan.dist_start+4],16)/10000
            scan.dist_data_amnt = int(data[scan.dist_start+5],16)
            scan.dist_end = (scan.dist_start+6) + scan.dist_data_amnt
            scan.distances = hex_to_meters(data[scan.dist_start+6:scan.dist_end])
            scan.raw_distances = " ".join(data[scan.dist_start+6:scan.dist_end])

        else:

            scan.dist_label = None
            scan.dist_scale_fact = None
            scan.dist_scale_fact_offset = None
            scan.dist_start_ang = None
            scan.dist_angle_res = None
            scan.dist_data_amnt = None
            scan.dist_end = None
            scan.distances = None
            scan.raw_distances = None

        if scan.rssi_start != None:

            scan.rssi_label = data[20]
            scan.rssi_scale_fact = int(data[scan.rssi_start+1],16)
            scan.rssi_scale_fact_offset = int(data[scan.rssi_start+2],16)
            scan.rssi_start_ang = uint32(data[scan.rssi_start+3])/10000
            scan.rssi_angle_res = int(data[scan.rssi_start+4],16)/10000
            scan.rssi_data_amnt = int(data[scan.rssi_start+5],16)
            scan.rssi_end = (scan.rssi_start+6) + scan.rssi_data_amnt
            scan.rssi = data[scan.rssi_start+6:scan.rssi_end]

        else:

            scan.rssi_label = None
            scan.rssi_scale_fact = None
            scan.rssi_scale_fact_offset = None
            scan.rssi_start_ang = None
            scan.rssi_angle_res = None
            scan.rssi_data_amnt = None
            scan.rssi_end = None
            scan.rssi = None

        return raw_data

# LMDscandata - reserved values PAGE 80

#####################################################################
#   Filter

def particle():    # Set particle filter
    # sWN LFPparticle 1 +500
    send('sWN LFPparticle')
    answer = read()
    return answer
    # sWA LFPparticle

def meanfilter(status_code=0,number_of_scans="+10"):    # Set mean filter
    # sWN LFPmeanfilter 1 +10 0
    send('sWN LFPmeanfilter '+status_code+' '+number_of_scans+' 0')
    answer = read()
    return answer
    # sWA LFPmeanfilter


#####################################################################
#   Outputs



def outputstate():    # Read state of the outputs
    # sRN LIDoutputstate
    send('sRN LIDoutputstate')

def eventoutputstate(state):    # Send outputstate by event
    send('sEN LIDoutputstate '+str(state))
    answer = read()
    return answer

def setoutput():    # Set output state
    # sMN mDOSetOutput 1 1
    send('sMN mDOSetOutput')
    answer = read()
    return answer
    # sAN mDOSetOutput 1
#####################################################################
#   Inputs

def debtim():    # Set debouncing time for input x
    # sWN DI3DebTim +10
    send('sWN DI3DebTim')
    answer = read()
    return answer
    # sWA DI3DebTim

def deviceident():    # Read device ident
    # sRN DeviceIdent
    send('sRN DeviceIdent')
    answer = read()
    answer = answer.split()
    answer = answer[3] + ' ' + answer[4] + ' ' + answer[5]
    return answer
    # sRA DeviceIdent 10 LMS10x_FieldEval 10 V1.36-21.10.2010

def devicestate():    # Read device state
    # sRN SCdevicestate
    send('sRN SCdevicestate')
    answer = read()
    return answer
    # sRA SCdevicestate 0

def ornr():    # Read device information
    # sRN DIornr
    send('sRN DIornr')
    answer = read()
    return answer
    # sRA DIornr 1071419

def devicetype():    # Device type
    # sRN DItype
    send('sRN DItype')
    answer = read()
    return answer
    # sRA DItype E TIM561-2050101

def oprh():    # Read operating hours
    # sRN ODoprh
    send('sRN ODoprh')
    answer = read()
    return answer
    # sRA ODoprh 2DC8B

def pwrc():    # Read power on counter
    # sRN ODpwrc
    send('sRN ODpwrc')
    answer = read()
    return answer
    # sRA ODpwrc 752D

def setLocationName(name):    # Set device name
    # sWN LocationName +13 OutdoorDevice
    name = " " + name
    string = 'sWN LocationName +'+str(len(name)-1)+name
    send(string)
    answer = read()
    return answer
    # sWA LocationName

def readLocationName():    # Read for device name
    # sRN LocationName
    send('sRN LocationName')
    answer = read()
    answer = parse_str(answer)
    return answer
    # sRA LocationName D OutdoorDevice

def rstoutpcnt():    # Reset output counter
    # sMN LIDrstoutpcnt
    send('sMN LIDrstoutpcnt')
    answer = read()
#    answer = parse_str(answer)
    return answer
    # sAN LIDrstoutpcnt 0

testing = demo_data()
print(testing)
