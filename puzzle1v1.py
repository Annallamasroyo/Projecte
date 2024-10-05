import RPi.GPIO
from adafruit_pn532 import *

class RfidReader:
	def __init__(self): #inicialitza el lector RFID/NFC del elechouse
		self.pn532 = PN532_UART(debug=False, reset=20)
		
	def inizialize(self):  #configura el PN532 per poder comunicar-se amb targetes MiFare
		try:
			self.pn532.SAM_configuration()
		except Exception as e:
			print(e)
			
	def read_uid(self):
		try:
			print('Esperant a la lectura de la tarjeta:')
			targeta = False #serveix per controlar que només detecti una targeta
			while True:
				uid = self.pn532.read_passive_target(0) #espera un temps indefinit fins que detecti una targeta
				if not targeta and uid is not None:
					targeta = True
					return "".join([hex(i).upper() for i in uid])
					#agafo cada string del uid i el converteixo en hexadecimal
					#de cada string borrem el "0x" del inici
					#paso a majuscules el string
		except Exception as e:
				print(e)
		
	def cleanup(self):
		GPIO.cleanup() #Neteja el GPIO al finalitzar
		
if __name__ == "__main__":
	try:
		RF = RfidReader()
		RF.inicialize()
		uid = RF.read_uid()
		print(uid)
	finally:
		RF.cleanup()
	
