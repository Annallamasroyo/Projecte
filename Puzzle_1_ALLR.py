import serial
import time
from adafruit_pn532 import uart

#Configura el port serial
ser = serial.Serial('/dev/serial0', baudrate=115200)

# Crea una instancia del PN532
pn532 = PN532_UART(ser)

# Inicia la comunicació
pn532.SAM_configuration()

print("Esperant a llegir targeta...")

while True:
    uid = pn532.read_passive_target()
    if uid is not None:
        # Converteix el UID en majuscules i hexadecimal
        uid_hex = [hex(i)[2:].upper() for i in uid]  #converteix cada byte en hex i treu '0x'
        uid_hex_str = ':'.join(uid_hex)
        print("UID: ", uid_hex_str)
        time.sleep(1) 
