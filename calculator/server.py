from threading import Thread
from calculator import PORT, bcolors
from calculator.client import Client

import socket
import traceback
import sys
import logging

class Server():
    # Initialises the code
    def __init__(self):
        logging.basicConfig(level=logging.NOTSET,
                    filename="calc.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
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
        logging.info('[SERVER] Socket now listening')

        while True:
            conn, addr = soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            logging.info('[SERVER] Accepting connection from ' + ip + ':' + port)
            try:
                client = Client()
                Thread(target=client.client_thread, args=(conn, ip, port)).start()
            except:
                logging.error('[SERVER] Unable to accept connection from ' + ip + ':' + port)
                traceback.print_exc()
        
        logging.info('[SERVER] Socket Closed')
        soc.close()