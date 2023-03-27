#!/usr/bin/env python3
import time
time.sleep(45)


import socket

import requests
from OpenBox import cajaNro

#Url de cintas LED
greenUrl1= 'http://sboxled1.local/win&R=0&G=255&B=0'
whiteUrl1= 'http://sboxled1.local/win&R=255&G=255&B=255'

greenUrl2= 'http://sboxled2.local/win&R=0&G=255&B=0'
whiteUrl2= 'http://sboxled2.local/win&R=255&G=255&B=255'

greenUrl3= 'http://sboxled3.local/win&R=0&G=255&B=0'
whiteUrl3= 'http://sboxled3.local/win&R=255&G=255&B=255'

greenUrl4= 'http://sboxled4.local/win&R=0&G=255&B=0'
whiteUrl4= 'http://sboxled4.local/win&R=255&G=255&B=255'

#Raspberry A
host = ""  #Hay que cambiar por raspberry
port =              #Hay que cambiar por raspberry

storedValue = "Get response"

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
    s.listen(4) # Allows four connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    reply = "default"
    print("Recibiendo Datos")
    # Receive the data
    try:
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
    except:
        print("Error al recibir datos")
        conn.close()
        return
    
        

    # Split the data such that you separate the command
    # from the rest of the data.
    dataMessage = data.split(' ', 1)
    command = dataMessage[0]

    print("mensaje: ", len(command))

    try:
        if (len(command) == 0):
            print("Ingreso vacio")
            reply = "Ingreso vacio"

        elif command == "BOX1":
            cajaNro(1)
            reply = "Abrimos caja 1"
            x = requests.get(whiteUrl1)
            print(x.status_code)
        elif command == "BOX2":
            cajaNro(2)
            reply = "Abrimos caja 2"
            x = requests.get(whiteUrl2)
            print(x.status_code)
        elif command == "BOX3":
            cajaNro(3)
            reply = "Abrimos caja 3"
            x = requests.get(whiteUrl3)
            print(x.status_code)
        elif command == "BOX4":
            cajaNro(4)
            reply = "Abrimos caja 4"
            x = requests.get(whiteUrl4)
            print(x.status_code)
        elif command == "GREEN1":
            x = requests.get(greenUrl1)
            print(x.status_code)
            reply = "Leds 1 verdes"
        elif command == "GREEN2":
            x = requests.get(greenUrl2)
            print(x.status_code)
            reply = "Leds 2 verdes"
        elif command == "GREEN3":
            x = requests.get(greenUrl3)
            print(x.status_code)
            reply = "Leds 3 verdes"
        elif command == "GREEN4":
            x = requests.get(greenUrl4)
            print(x.status_code)
            reply = "Leds 4 verdes"
            
        elif command == 'GET':
            reply = GET()
        elif command == 'EXIT':
            print("Our client has left us :(")
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
        else:
            print("No encontramos el comando ingresado")
            
        
    except:
        reply = "Error al abrir caja"
        
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
        time.sleep(1)
        break
