import binascii
import struct
import pynfc

class RfidPyNFC:
    def __init__(self):
        #self.nfc = pynfc.Nfc("pn532_uart:/dev/ttyS0:115200")
        self.nfc = pynfc.Nfc()
    
    def read_uid(self):
        print("Esperant per lleguir targeta...")
        # poll() returns a generator, __next__ is python3
        target = self.nfc.poll().__next__()
        return target.uid.decode('ascii').upper()

if __name__ == "__main__":
    rf = RfidPyNFC()
    uid = rf.read_uid()
    print("S'ha detectat una targeta i el seu UID es:")
    print(uid)

