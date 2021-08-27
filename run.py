from socket import *
import json, time
import threading



class Test():

    def __init__(self):
        t1 = threading.Thread(target=self._equipment_a1,args=())
        t1.start()
        t2 = threading.Thread(target=self._equipment_a2,args=())
        t2.start()

    def _toData(self, callback):
        data = []
        for i in range(len(callback)):
            data.append((i,str(callback[i])))
        return data

    def _equipment_a1(self):
        
        addr = ('192.168.1.112',8899)
        tcpsocket = socket(AF_INET,SOCK_STREAM)
        tcpsocket.connect(addr)

        e1_runcount = 0
        
        while True:
            
            tcpsocket.send(bytearray.fromhex("01 06 00 1A 00 01 69 CD"))
            time.sleep(2)
            tcpsocket.send(bytearray.fromhex("01 03 00 1A 00 01 A5 CD"))
            callback = tcpsocket.recv(1024)
            print(">[1]开, recv: ", self._toData(callback))
            time.sleep(1)
            

            tcpsocket.send(bytearray.fromhex("01 06 00 1A 00 00 A8 0D"))
            time.sleep(2)
            tcpsocket.send(bytearray.fromhex("01 03 00 1A 00 01 A5 CD"))
            callback2 = tcpsocket.recv(1024)
            print(">[1]关, recv: ", self._toData(callback2))
            time.sleep(1)

            e1_runcount = e1_runcount + 1

            print("[equipment-1] run count", e1_runcount)

    def _equipment_a2(self):
        addr = ('192.168.1.172',8899)
        tcpsocket = socket(AF_INET,SOCK_STREAM)
        tcpsocket.connect(addr)

        e2_runcount = 0

        while True:

            tcpsocket.send(bytearray.fromhex("02 06 00 1A 00 01 69 FE"))
            time.sleep(1)
            tcpsocket.send(bytearray.fromhex("02 03 00 1A 00 01 A5 FE"))
            callback = tcpsocket.recv(1024)
            print(">[2]开, recv: ", self._toData(callback))
            time.sleep(1)
            

            tcpsocket.send(bytearray.fromhex("02 06 00 1A 00 00 A8 3E"))
            time.sleep(1)
            tcpsocket.send(bytearray.fromhex("02 03 00 1A 00 01 A5 FE"))
            callback2 = tcpsocket.recv(1024)
            print(">[2]关, recv: ", self._toData(callback2))
            time.sleep(1)

            e2_runcount = e2_runcount + 1
            
            print("[equipment-2] run count", e2_runcount)

if __name__ == '__main__':
    Test()