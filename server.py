#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os
import os.path


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            print "El cliente nos manda " + line
            Metodos = ["INVITE", "ACK", "BYE"]
            Metodo = line.split(" ")[0]
            Mensaje = line.split(" ")
            IP_CLIENT = str(self.client_address[0])
            if len(Mensaje) == 3:
                if Metodo in Metodos:
                    if Metodo == "INVITE":
                        Answer = "SIP/2.0 100 Trying\r\n\r\n"
                        Answer += "SIP/2.0 180 Ring\r\n\r\n"
                        Answer += "SIP/2.0 200 OK\r\n\r\n"
                        self.wfile.write(Answer)
                    elif Metodo == "ACK":
                        fichero_audio = sys.argv[3]
                        aEjecutar = "./mp32rtp -i " + IP_CLIENT + " -p 23032 < "
                        aEjecutar += fichero_audio
                        print "Vamos a ejecutar", aEjecutar
                        os.system("chmod 755 mp32rtp")
                        os.system(aEjecutar)
                    elif Metodo == "BYE":
                        Answer = "SIP/2.0 200 OK\r\n\r\n"
                        self.wfile.write(Answer)
                else:
                    Answer = "SIP/2.0 405 Method Not Allowed\r\n\r\n"
                    self.wfile.write(Answer)
            else:
                Answer = "SIP/2.0 400 Bad Request\r\n\r\n"
                self.wfile.write(Answer)

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")
    if not os.path.exists(sys.argv[3]):
        sys.exit("El archivo " + sys.argv[3] + " no existe")
    serv = SocketServer.UDPServer(("", int(sys.argv[2])), EchoHandler)
    print "Listening..."
    serv.serve_forever()
