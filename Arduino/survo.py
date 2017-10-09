
import serial



def init_serial():
	ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
	return ser


def send_signal(ser, signal):
	ret = ser.write(signal)
	print("return value : ", ret)
	 


		
	
