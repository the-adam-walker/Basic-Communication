#Author: Adam Walker
#Python: v2.7.0
#Date: 2/8/2020
#Version: 1.0

import serial  # Allows for read from the serial port
import logging # Allows for logging of data 

port = "/dev/serial0"


current_location = {  # Dictionary used to format and store data
	'time'   : 'NA',
	'lat'    : 'NA',
	'dirLat' : 'NA',
	'lon'    : 'NA',
	'dirLon' : 'NA',
	'speed'  : 'NA',
	'trCouse': 'NA',
	'date'   : 'NA'
}


def updateDictionary(data): # Updates the current_location dictionary with the correct NMEA sentence (GNRMC)
    if data[0:6] == "$GNRMC":
        sdata = data.split(",")
        if sdata[2] == 'V':
            logging.info("no satellite data available")
            return
        current_location['time'] = sdata[1][0:2] + ":" + sdata[1][2:4] + ":" + sdata[1][4:6]
        current_location['lat'] = decode(sdata[3]) #latitude
        current_location['dirLat'] = sdata[4]      #latitude direction N/S
        current_location['lon'] = decode(sdata[5]) #longitute
        current_location['dirLon'] = sdata[6]      #longitude direction E/W
        current_location['speed'] = sdata[7]       #Speed in knots
        current_location['trCourse'] = sdata[8]    #True course
        current_location['date'] = sdata[9][0:2] + "/" + sdata[9][2:4] + "/" + sdata[9][4:6]#date
	logging.info(current_location)

def decode(coord): # Converts DDDMM.MMMMM > DD deg MM.MMMMM min
    x = coord.split(".")
    head = x[0]
    tail = x[1]
    deg = head[0:-2]
    min = head[-2:]
    return deg + " deg " + min + "." + tail + " min"


logging.basicConfig(filename='FireWatch/log.txt', filemode='w', level=logging.INFO)
logging.info("Receiving GPS data")
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while (1):
	data = ser.readline()
	updateDictionary(data)

