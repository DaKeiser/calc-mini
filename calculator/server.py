from threading import Thread
from calculator import PORT, bcolors
from calculator.client import Client

import socket
import traceback
import sys
import logging

class Server():
    def __init__(self):
        pass

    def start_server(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        logging.info('[SERVER] Socket created')

        try:
            soc.bind(("0.0.0.0", PORT))
            logging.info('[SERVER] Socket bind complete')
        except socket.error as msg:
            logging.error('[SERVER] Socket bind error ' + str(sys.exc_info()))
            sys.exit()

        soc.listen(10)
        print('-'*50)
        print("Welcome to the Mini-Calculator server")
        print("Connect here using the command `nc server_ip 6969`")
        print('-'*50)
        print('Socket now listening')

        while True:
            conn, addr = soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            logging.info('[SERVER] Accepting connection from ' + ip + ':' + port)
            print('Accepting connection from ' + ip + ':' + port)
            try:
                client = Client()
                Thread(target=client.client_thread, args=(conn, ip, port)).start()
            except:
                logging.error('[SERVER] Unable to accept connection from ' + ip + ':' + port)
                print("Terible error!")
                traceback.print_exc()
        
        logging.info('[SERVER] Socket Closed')
        soc.close()