import serial
import time
import pygame
import threading
import sys
 
pygame.init()
 
display = pygame.display.set_mode((300, 300))

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM24"

connection = False

while not connection:
    try:
        ser.open()
        print('Connected!')
        ser.write("CONNECT".encode())
        connection = True
    except:
        sys.exit()

def read_serial():
    while True:
        rcv = ser.readline()
        if rcv:
            cmd = rcv.decode('utf-8').rstrip()
            print(cmd)
            print(rcv)

serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()

b_button_prev_state = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ser.write("OFF".encode())
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            print("The 'w' key is being held down")
            ser.write("w".encode())

        if keys[pygame.K_a]:
            print("The 'a' key is being held down")
            ser.write("a".encode())

        if keys[pygame.K_s]:
            print("The 's' key is being held down")
            ser.write("s".encode())

        if keys[pygame.K_d]:
            print("The 'd' key is being held down")
            ser.write("d".encode())
        if keys[pygame.K_p]:
     
            print("B button pressed")
            ser.write("BB".encode())

    time.sleep(0.1)
 
    pygame.display.update()
    
