from ensurepip import version
import re
from cv2 import getFontScaleFromHeight

from numpy import mat

import json


def GetGroup(text: str, regex) -> str:
    match = re.search(regex, text)
    if match is None:
        return 'NO INFO'
    return match.group(1)


reInstallStart = re.compile(
    r">>>  \[Device Install \(Hardware initiated\) \- ([0-9\w \\#{}\-\.\?_\/&]+)\]")
reInstallEnd = re.compile(r"<<<  \[Exit status: \w+\]")
reVendor = re.compile(r"Ven_([\w]+)")
reProd = re.compile(r"Prod_([\w]+)")
reRev = re.compile(r"Rev_([\w\.]+)")
reTime = re.compile(r">>>  Section start ([\w\/ :\.]+)")
reDevDesc = re.compile(r"\s+dvi:\s+DevDesc\s+\- ([\w ]+)")
reDrvDate = re.compile(r"\s+dvi:\s+DrvDate\s+\- ([\w// ]+)")
reVersion = re.compile(r"\s+dvi:\s+Version\s+\- ([\w\. ]+)")

lstDevices = []
with open('setupapi.dev.log', 'r') as file: 
    data = file.read()
    allInstallStart = re.finditer(reInstallStart, data)

    for deviceStartMatch in allInstallStart:
        currentBlockStart = deviceStartMatch.start()
        temp = data[currentBlockStart:]
        endMatch = re.search(reInstallEnd, temp)
        currentBlockEnd = endMatch.start() + currentBlockStart

        currentDataBlock = data[currentBlockStart: currentBlockEnd]

        deviceInfo = deviceStartMatch.group(1)
        info = {
            'Device Info': deviceInfo,
            'Product': GetGroup(deviceInfo, reProd),
            'Vendor': GetGroup(deviceInfo, reVendor),
            'Revision': GetGroup(deviceInfo, reRev),
            'Connected Time': GetGroup(currentDataBlock, reTime),
            'Dev. Description': GetGroup(currentDataBlock, reDevDesc),
            'Driver Date': GetGroup(currentDataBlock, reDrvDate),
            'Driver Version': GetGroup(currentDataBlock, reVersion)
        }
            
        lstDevices.append(info)
        
        print(json.dumps(info, indent=4))
        print('='*16)


with open('output.txt', 'w') as file:
    file.writelines([json.dumps(x, indent=4) for x in lstDevices])
    
