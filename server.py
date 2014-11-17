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
                if not Method in MethodList:
                    print "Enviando: SIP/2.0 405 Method Not Allowed"
                    self.wfile.write('SIP/2.0 405 Method Not Allowed\r\n')
                    break  # Se detiene. Error específico.
                if Method == "INVITE":
                    print "Enviando: SIP/2.0 100 Trying"
                    self.wfile.write('SIP/2.0 100 Trying\r\n')
                    print "Enviando: SIP/2.0 180 Ring"
                    self.wfile.write('SIP/2.0 180 Ring\r\n')
                    print "Enviando: SIP/2.0 200 OK"
                    self.wfile.write('SIP/2.0 200 OK\r\n')
                elif Method == "ACK":
                    #iniciar RTP
                    print "Enviando: Transmisión de datos terminada"
                    self.wfile.write('Transmisión de datos terminada\r\n')
                elif Method == "BYE":
                    print "Enviando: SIP/2.0 200 OK"
                    self.wfile.write('SIP/2.0 200 OK\r\n')
                else:
                    print "Enviando: SIP/2.0 400 Bad Request"
                    self.wfile.write('SIP/2.0 400 Bad Request\r\n')
                    # Error general


if __name__ == "__main__":
    try:
        IP = sys.argv[1]
        PORT = sys.argv[2]
        SONG = sys.argv[3] #COMPROBAR QUE EXISTE
    except IndexError:
        sys.exit('Usage: python server.py IP port audio_file')
    except ValueError:
        sys.exit('Usage: python server.py IP port audio_file')

    MethodList = ["INVITE", "ACK", "BYE"]
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", int(PORT)), EchoHandler)
    print "Listening..."
    serv.serve_forever()
