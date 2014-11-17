#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        print "El cliente " + str(self.client_address) + " nos manda:"
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo mensaje a mensaje lo que nos envía el cliente
            line = self.rfile.read()
            if not line:
                break
            else:
                print line
                WordList = line.split(' ')
                Method = WordList[0]
                if Method == "INVITE":
                elif Method == "ACK":
                elif Method == "BYE":
                else:
                #SIP/2.0 400 Bad Request o SIP/2.0 405 Method Not Allowed ??


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    try:
        IP = sys.argv[1]
        PORT = sys.argv[2]
        SONG = sys.argv[3] #COMPROBAR QUE EXISTE
    except IndexError:
        sys.exit('Usage: python server.py IP port audio_file')
    except ValueError:
        sys.exit('Usage: python server.py IP port audio_file')
    serv = SocketServer.UDPServer(("", int(PORT)), EchoHandler)
    print "Listening..."
    serv.serve_forever()
