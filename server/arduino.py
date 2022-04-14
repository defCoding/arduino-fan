import time
import serial
import threading

DEVICE = '/dev/cu.usbmodem1101'

def wait_for_arduino(ser):
    msg =  ""
    while msg.find("Arduino is ready") == -1:
        while ser.in_waiting == 0:
            continue
        msg = ser.readline().decode('ascii')

def send_byte(i, /):
    ser.write(i.to_bytes(1, 'big'))

def initialize(ser):
    ser.reset_input_buffer()
    wait_for_arduino(ser)
    ser.reset_output_buffer()

ser = serial.Serial(DEVICE, 9600)
thr = threading.Thread(target=initialize, args=[ser])
thr.start()
