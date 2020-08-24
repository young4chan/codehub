import socket
ip = '127.0.0.1'
port = 9911
sockedfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockedfd.settimeout(1)
sockedfd.bind(('', 10000))


pos_mark = 0

with open(r"01.bin", "rb") as f:
    while True:
        header = f.read(8)
        if header == b'\x02\x01\x04\x03\x06\x05\x08\x07':
            #print("yes")
            pass
        f.seek(pos_mark + 16, 0)
        detNum = f.read(2)
        detNum = int.from_bytes(detNum, byteorder='little', signed=False)
        trkNum = f.read(2)
        trkNum = int.from_bytes(trkNum, byteorder='little', signed=False)
        
        handshake = b'\x01\x09\x08\x09\x01\x00\x02\x02'
        handshakeFrameLen = (48 + detNum * 16 + trkNum * 32 + 32)
        #print('frame length: ' + str(handshakeFrameLen))
        handshakeFrameLenBytes = (48 + detNum * 16 + trkNum * 32 + 32).to_bytes(4, byteorder = 'little')
        handshakeReserved = b'\x00' * 12
        handshake = handshake + handshakeFrameLenBytes + handshakeReserved
        count = sockedfd.sendto(handshake, (ip, port))                          # send out handshake pkg
        
        f.seek(pos_mark, 0)
        for i in range(handshakeFrameLen//256):
            data = f.read(256)                                                  # send out package of the length of 256 bytes
            count = sockedfd.sendto(data, (ip, port))
            if count != 256:
                #print("Error in sending package")
                pos_mark = 0
                f.seek(pos_mark, 0)
        data = f.read(handshakeFrameLen % 256)
        count = sockedfd.sendto(data, (ip, port))                               # send out the remaining package of one frame
        if count != handshakeFrameLen % 256:
            #print("Error in sending package")
            pos_mark = 0
            f.seek(pos_mark, 0)
        else:
            pos_mark += handshakeFrameLen

print('file sending finish')
'''  
    print('handshake: ')
    print(handshake)
    print('detNum: ')
    print(detNum)
    print('trkNum: ')
    print(trkNum)
    print(type(header))
    print(header)
'''