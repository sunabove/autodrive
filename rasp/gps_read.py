import serial
ser = serial.Serial("/dev/ttyS0", 9600)
while 1 :
     try : 
     	cc=str(ser.readline())
     	print(cc[2:][:-5], end='')
     except :
        pass
