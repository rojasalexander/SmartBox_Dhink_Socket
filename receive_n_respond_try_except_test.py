#!/usr/bin/env python3
import time
import logging

time.sleep(45)

import socket

import requests
# from OpenBox import cajaNro

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
host = "192.168.111.14"   #Hay que cambiar por raspberry
port = 5005             #Hay que cambiar por raspberry

storedValue = "Sergio es Dios probando"

logging.basicConfig( filename = "smartbox.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.debug('Se prendio el smartbox')


def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    logging.debug('Se inicializo el servidor')
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
        logging.debug(str(msg))
    except socket.timeout as tmt:
        print(tmt)
        logging.debug(str(tmt))
    print("Socket bind complete.")
    logging.debug('Conexion establecida')
    return s

def setupConnection():
    s.listen(4) # Allows two connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    logging.debug("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    logging.debug("RECIBIMOS REQUEST")
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    reply = "Se recibio el comando"
    logging.debug('Se recibio el comando')
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
    logging.debug("El comando recibido es:" + str(command))

    try:
        if (len(command) == 0):
            print("Ingreso vacio")
            reply = "Ingreso vacio"
            logging.debug('Ingreso vacio')

        elif command == "BOX1":
            #cajaNro(1)
            reply = "Abrimos caja 1"
            logging.debug('Abrimos caja 1')
            try:
                logging.debug("LUCES BLANCAS")
                #x = requests.get(whiteUrl1)
                #print(x.status_code)
            except:
                print("Error al abrir caja 1")
                logging.warning('Error al abrir la caja 1')
        elif command == "BOX2":
            #cajaNro(2)
            reply = "Abrimos caja 2"
            logging.debug('Abrimos caja 2')
            try:
                logging.debug("LUCES BLANCAS")
                #x = requests.get(whiteUrl2)
                #print(x.status_code)
            except:
                print("Error al abrir caja 2")
                logging.warning('Error al abrir la caja 2')
        elif command == "BOX3":
            #cajaNro(3)
            reply = "Abrimos caja 3"
            logging.debug('Abrimos caja 3')
            try:
                logging.debug("LUCES BLANCAS")
                #x = requests.get(whiteUrl3)
                #print(x.status_code)
            except:
                print("Error al abrir caja 3")
                logging.warning('Error al abrir la caja 3')
        elif command == "BOX4":
            #cajaNro(4)
            reply = "Abrimos caja 4"
            logging.debug('Abrimos caja 4')
            try:
                logging.debug("LUCES BLANCAS")
                #x = requests.get(whiteUrl4)
                #print(x.status_code)
            except:
                print("Error al abrir caja 4")
                logging.warning('Error al abrir la caja 4')
        elif command == "GREEN1":
            try:
                #x = requests.get(greenUrl1)
                #print(x.status_code)
                reply = "Leds 1 verdes"
                logging.debug('Cambio LED 1 a verdes')
            except:
                print("Error al cambiar leds 1 a verdes")
                logging.warning('Error al cambiar los leds 1 a verdes')
        elif command == "GREEN2":
            try:
                #x = requests.get(greenUrl2)
                #print(x.status_code)
                reply = "Leds 2 verdes"
                logging.debug('Cambio LED 2 a verdes')
            except:
                print("Error al abrir caja 2")
                logging.warning('Error al cambiar los leds 2 a verdes')
        elif command == "GREEN3":
            try:
                #x = requests.get(greenUrl3)
                #print(x.status_code)
                reply = "Leds 3 verdes"
                logging.debug('Cambio LED 3 a verdes')
            except:
                print("Error al abrir caja 3")
                logging.warning('Error al cambiar los leds 3 a verdes')
        elif command == "GREEN4":
            try:
                #x = requests.get(greenUrl4)
                #print(x.status_code)
                reply = "Leds 4 verdes"
                logging.debug('Cambio LED 4 a verdes')
            except:
                print("Error al abrir caja 4")
                logging.warning('Error al cambiar los leds 4 a verdes')
            
        elif command == 'GET':
            reply = GET()
        elif command == 'EXIT':
            print("Our client has left us :(")
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
        else:
            print("No encontramos el comando ingresado")
            logging.warning('No existe el comando ingresado')
            
        
    except:
        reply = "Error al abrir caja"
        logging.warning('Error al abrir caja')
        
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
        
