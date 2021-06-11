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
