import binascii #convertir de binari a hexadecimal
from adafruit_pn532.i2c import PN532_I2C
import busio
import board
import time
from digitalio import DigitalInOut
import RPi.GPIO as GPIO


class RfidReader:
	def __init__(self):
		reset_pin = DigitalInOut(board.D6)
		req_pin = DigitalInOut(board.D12)
		i2c= busio.I2C(board.SCL, board.SDA)
		self.pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)
		self.pn532.SAM_configuration()
			
	def read_uid(self):
		print("Esperant a lleguir targeta...")
		uid = self.pn532.read_passive_target(0)
		if uid is not None:
			return binascii.hexlify(uid).decode("utf-8").upper()
			
		else:
			print("No s'ha detectat cap targeta...")
			return None				
		
			
	def cleanup(self):
		# Neteja els recursos del GPIO 
		GPIO.cleanup()
		
if __name__ == "__main__":
	try:
		rf = RfidReader()		
		uid = rf.read_uid()
		
		if(uid):
			print("UID: " , uid)
			
	finally:
		rf.cleanup()

	
