from pyfirmata import Arduino, util, STRING_DATA
board = Arduino('/dev/ttyUSB0')
board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('ola!') )

