#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
try:
    Method = sys.argv[1].upper()
    NAME = sys.argv[2].split('@')[0]
    SERVER = sys.argv[2].split('@')[1].split(':')[0]
    PORT = sys.argv[2].split('@')[1].split(':')[1]
except IndexError:
    sys.exit('Usage: python client.py method receiver@IP:SIPport')
except ValueError:
    sys.exit('Usage: python client.py method receiver@IP:SIPport')

# Contenido que vamos a enviar
Line = Method + ' sip:' + NAME + '@' + SERVER + ' SIP/2.0'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, int(PORT)))

try:
    print "Enviando: " + Line
    my_socket.send(Line + '\r\n')
    data = my_socket.recv(1024)
except:
    sys.exit('Error: No server listening at ' + SERVER + ' port ' + PORT)

print 'Recibido -- \r\n', data
ListaTexto = data.split('\r\n')
if Method == "INVITE":
    if ListaTexto[2] == 'SIP/2.0 200 OK':
        Method = "ACK"
        Line = Method + ' sip:' + NAME + '@' + SERVER + ' SIP/2.0'
        print "Enviando: " + Line
        my_socket.send(Line + '\r\n')
# Si estamos en BYE directamente nos salimos tras imprimir data

print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
