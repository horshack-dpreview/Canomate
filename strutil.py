#!/usr/bin/env python3

#
#############################################################################
#
# strutil - String utility functions
# Copyright (C) 2020, Horshack
#
# This module is licensed under GPL v3: http://www.gnu.org/licenses/gpl-3.0.html
#
#############################################################################
#

import struct
import sys
import time

#
# returns a date/time string in mm/dd/yy hh:mm:ss format for specified
# epoch time - if epoch time is None then returns date/time string for
# current time
#
def getDateTimeStr(timeEpoch=None, fMilitaryTime=True):
    if timeEpoch == None:
        timeEpoch = time.time()
    timeStruct = time.localtime(timeEpoch)
    if not fMilitaryTime:
        timeStr = time.strftime("%m/%d/%y %I:%M:%S %p", timeStruct)
    else:
        timeStr = time.strftime("%m/%d/%y %H:%M:%S", timeStruct)
    return timeStr


#
# Generates string containing hex dump of a bytearray. Format is:
#
# bytesPerField=1:
#
#   <offset>: xx xx xx xx xx xx xx xx - xx xx xx xx xx xx xx xx yyyyyyyy - yyyyyyyy
#
# bytesPerField=2:
#
#   <offset>: xxxx xxxx xxxx xxxx - xxxx xxxx xxxx xxx yyyyyyyy - yyyyyyyy
#
# bytesPerField=4:
#
#   <offset>: xxxxxxxx xxxxxxxx - xxxxxxxx xxxxxxx yyyyyyyy - yyyyyyyy
#
# Where 'xx' are the hex values of each byte/halfword/word and 'y' is
# the ASCII character equivalent ('.' for each non-printable ASCII value <32 or >127)
#
def hexdump(data, bytesPerField=1, includeASCII=1):
    bytesPerFieldToUnpackStr = { 1 : 'B', 2 : 'H', 4 : 'I', 8 : 'Q' }
    strHexDump=''
    if bytesPerField not in bytesPerFieldToUnpackStr:
        raise AssertionError("hexdump: bytesPerField invalid. must be 1, 2, 4, or 8");
    if (len(data) % bytesPerField) != 0:
        raise AssertionError("hexdump: size of data (0x{:04x}) is not a multiple of bytesPerField ({:d})".format(len(data), bytesPerField))
    for offset in xrange(0,len(data),bytesPerField):
        offsetThisFieldInLine = (offset % 16)   # byte offset into data for this field of current line
        endingOffsetThisFieldInLine = offsetThisFieldInLine + bytesPerField
        if (offsetThisFieldInLine == 0):
            strHexDump += "{:04x}: ".format(offset)
        (thisField,) = struct.unpack(bytesPerFieldToUnpackStr[bytesPerField], data[offset:offset+bytesPerField])
        strHexDump += "{:0{:d}x} ".format(thisField, bytesPerField*2)       # (value,width) - width: bytes=2, halfwords=4, words=8
        if (endingOffsetThisFieldInLine == 8):
            strHexDump += "- "
        if (endingOffsetThisFieldInLine == 16 or (offset==len(data)-1)):
            # just processed 16 bytes of line or have reached final byte
            # of buffer (partial last line). Add ASCII representation
            # of hex values on this line.
            bIsFinalLine = (offset == len(data)-1)
            if includeASCII:
                if (endingOffsetThisFieldInLine < 16):
                    # final line is a partial line. pad with spaces to
                    # fill out area that would normally contain hex
                    # values before start ASCII dump seciton
                    fieldsNotPrintedInFinalLine = (16-endingOffsetThisFieldInLine) * bytesPerField
                    charactersPerFieldIncludingSpace = bytesPerField*2 + 1
                    strHexDump += " " * (fieldsNotPrintedInFinalLine*charactersPerFieldIncludingSpace) # add spaces for each missing field
                    if (endingOffsetThisFieldInLine < 8):
                        strHexDump += "  "                              # add spaces for missing middle separator
                for asciiOffset in range(offsetThisFieldInLine+1):
                    (thisByte,) = struct.unpack('B', data[offset-offsetThisFieldInLine+asciiOffset:offset-offsetThisFieldInLine+asciiOffset+1])
                    if (thisByte >= 32 and thisByte <= 127):
                        strHexDump += six.unichr(thisByte)
                    else:
                        strHexDump += "."
                    if (asciiOffset == 7):
                        strHexDump += " - "
            if not bIsFinalLine:    # don't put newline after final line
                strHexDump += "\n"
    return strHexDump

