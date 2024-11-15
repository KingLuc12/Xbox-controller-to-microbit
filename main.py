import serial
import time
import pygame
import threading
import sys
 
pygame.init()
 
display = pygame.display.set_mode((300, 300))

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"

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

if pygame.joystick.get_count() == 0:
    print("No joystick connected!")
    pygame.quit()
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick Name: {joystick.get_name()}")
print(f"Number of Axes: {joystick.get_numaxes()}")
print(f"Number of Buttons: {joystick.get_numbuttons()}")
print(f"Number of Hats: {joystick.get_numhats()}")

b_button_prev_state = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ser.write("OFF".encode())
            pygame.quit()
            sys.exit()
        button_A = joystick.get_button(0)  
        button_B = joystick.get_button(1)  
        button_X = joystick.get_button(2)  
        button_Y = joystick.get_button(3) 

    
        if button_A:
            print("A button pressed")
        if button_X:
            print("X button pressed")
        if button_Y:
            print("Y button pressed")

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
            hat = joystick.get_hat(0) 
    if button_B and not b_button_prev_state:
     
        print("B button pressed")
        ser.write("BB".encode())
     
    hat = joystick.get_hat(0)

    if hat != (0, 0):
        # Write specifc D-pad directions to SERIAL
        print(f"D-pad direction: {hat}")
        print(hat)
        if (hat == (0, 1)):
            ser.write('w'.encode())
        if (hat == (-1, 0)):
            ser.write('a'.encode())
        if (hat == (0, -1)):
            ser.write('s'.encode())
        if (hat == (1, 0)):
            ser.write('d'.encode())

    time.sleep(0.1)
 
    pygame.display.update()
    
