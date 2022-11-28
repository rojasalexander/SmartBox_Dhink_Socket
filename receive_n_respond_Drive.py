import time
time.sleep(45)

import serial
import socket

import requests

#Raspberry B
host = "192.168.101.17"
port = 5005

storedValue = "Sergio es Dios"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    return reply

def abrir():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(1)

    for i in range(2):
        if i == 1:
            ser.write(b"ABRIR\n")
        print(ser.readline().decode('utf-8').rstrip())
        time.sleep(1)
        
        
def cerrar():          
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(1)

    for i in range(2):
        if i == 1:
            ser.write(b"CERRAR\n")
        print(ser.readline().decode('utf-8').rstrip())
        time.sleep(1)

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        if (data == b''):
            print("Ingreso vacio")
            break
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        
        print("mensaje: ", command)
        
        try:
            if command == "ABRIR":
                #motor hacia la derecha                
                abrir()
                reply = "Abrimos el smartbox"
                
            elif command == "CERRAR":
                #motor hacia la izquierda                
                cerrar()
                reply = "Cerramos el smartbox"
                    
            elif command == 'GET':
                reply = GET()
            elif command == 'EXIT':
                print("Our client has left us :(")
                break
            elif command == 'KILL':
                print("Our server is shutting down.")
                s.close()
                break
            else:
                print("Our server is shutting down.")
                break
            
        except:
            reply = "Error al abrir caja"
            break
        

        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()
        

s = setupServer()

while True:
    time.sleep(0.5)
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
