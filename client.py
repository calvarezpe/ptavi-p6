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
    METHOD = sys.argv[1]
    NAME = sys.argv[2].split('@')[0]
    SERVER = sys.argv[2].split('@')[1].split(':')[0]
    PORT = sys.argv[2].split('@')[1].split(':')[1]
except IndexError:
    sys.exit('Usage: python client.py method receiver@IP:SIPport')
except ValueError:
    sys.exit('Usage: python client.py method receiver@IP:SIPport')

# Contenido que vamos a enviar
LINE = METHOD + ' sip:' + NAME + '@' + SERVER + ' SIP2.0'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, int(PORT)))

try:
    print "Enviando: " + LINE
    my_socket.send(LINE + '\r\n')
    data = my_socket.recv(1024)
except:
    sys.exit('Error: No server listening at ' + SERVER + ' port ' + PORT)

print 'Recibido -- \r\n', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
