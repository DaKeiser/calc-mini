import os
import time
import sys

from calculator import MAX_TIME, bcolors
from calculator.calculator import Calculator
import logging

class Client():
    def __init__(self):
        self.calc = Calculator()
        self.banner = f'{bcolors.HEADER}{os.linesep}\
╔═══╗──╔╗──────╔╗───╔╗{os.linesep}\
║╔═╗║──║║──────║║──╔╝╚╗{os.linesep}\
║║─╚╬══╣║╔══╦╗╔╣║╔═╩╗╔╬══╦═╗{os.linesep}\
║║─╔╣╔╗║║║╔═╣║║║║║╔╗║║║╔╗║╔╝{os.linesep}\
║╚═╝║╔╗║╚╣╚═╣╚╝║╚╣╔╗║╚╣╚╝║║{os.linesep}\
╚═══╩╝╚╩═╩══╩══╩═╩╝╚╩═╩══╩╝{os.linesep}\
{bcolors.OKGREEN}Developed by Sai Rithwik M{os.linesep}\
{bcolors.OKGREEN}IMT2018061{os.linesep}\
{bcolors.OKGREEN}As part of CS 816 - Software Production Engineering course.{os.linesep}\
**************************************************{os.linesep}\
{os.linesep}\
'.encode()

        self.message = f'{bcolors.OKBLUE}{os.linesep}\
This is a simple calculator with which you can perform the following functions:{os.linesep}\
1) Find Square Root of a number{os.linesep}\
2) Find Factorial of a number{os.linesep}\
3) Find Common Logarithm of a number log₁₀{os.linesep}\
4) Find Natural Logarithm of a number logₑ{os.linesep}\
5) Find a number raised to another number{os.linesep}\
6) Exit{os.linesep}\
{os.linesep}\
{bcolors.BOLD}Choose a valid option from 1-6: '.encode()

        self.misc = '''
The miscellaneous functions we provide are
a) Addition of 2 numbers
b) Subtraction of a number from another number
c) Multiplication of a number by another number
d) Division of a number from another

Choose a valid option from a-d: '''.encode()

        self.large_input = f'{bcolors.FAIL}{os.linesep}\
I see you have sent too large input.{os.linesep}\
Please try again{os.linesep}\
'.encode()

    def integer_check(self, conn, n):
        try:
            guess = int(n.decode("utf8").rstrip())
            return guess
        except ValueError:
            conn.sendall(f"{bcolors.FAIL}That's not an int!\n".encode())
            conn.sendall(b"________________________________________\n\n")
            return -1

        # func_op = n.decode("utf8").rstrip()
        # if type(func_op) == int:
        #     return int(func_op)

        # # Check this part of the code
        # else:
        #     logging.error("[CLIENT] Input sent is not an integer")
        #     conn.sendall(b"Input sent is not an integer\n")
        #     return -1

    def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):
        conn.sendall(self.banner)
        start = time.time()

        while True:

            if time.time()-start > MAX_TIME: 
                conn.sendall(f"\nTime Limit Exceeded !!!!\n".encode()) 
                break

            conn.sendall(self.message)

            input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)
            siz = sys.getsizeof(input_from_client_bytes)

            if  siz >= MAX_BUFFER_SIZE:
                logging.error("[CLIENT] Reached MAX_BUFFER_SIZE")
                conn.send(self.large_input)
                continue

            # Ask for type of operation
            else:
                func_op = self.integer_check(conn, input_from_client_bytes)
                if func_op != -1:
                    if func_op == 1:
                        conn.sendall(b"SQRT: Enter a number: ")
                        inp_n = conn.recv(1024)
                        n = self.integer_check(conn, inp_n)
                        if func_op != -1:
                            ans = self.calc.squrt(n)
                            conn.sendall(f"\n{bcolors.OKGREEN}OUTPUT: ".encode() + str(ans).encode())
                        else:
                            continue
                    elif func_op == 2:
                        conn.sendall(b"FACTORIAL: Enter a number: ")
                        inp_n = conn.recv(1024)
                        n = self.integer_check(conn, inp_n)
                        if func_op != -1:
                            ans = self.calc.factorial(n)
                            conn.sendall(f"\n{bcolors.OKGREEN}OUTPUT: ".encode() + str(ans).encode())
                        else:
                            continue
                    elif func_op == 3:
                        conn.sendall(b"LOG: Enter a number: ")
                        inp_n = conn.recv(1024)
                        n = self.integer_check(conn, inp_n)
                        if func_op != -1:
                            ans = self.calc.log(n)
                            conn.sendall(f"\n{bcolors.OKGREEN}OUTPUT: ".encode() + str(ans).encode())
                        else:
                            continue
                    elif func_op == 4:
                        conn.sendall(b"LN: Enter a number: ")
                        inp_n = conn.recv(1024)
                        n = self.integer_check(conn, inp_n)
                        if func_op != -1:
                            ans = self.calc.ln(n)
                            conn.sendall(f"\n{bcolors.OKGREEN}OUTPUT: ".encode() + str(ans).encode())
                        else:
                            continue
                    elif func_op == 5:
                        conn.sendall(b"POWER: Enter the base: ")
                        inp_n1 = conn.recv(1024)
                        conn.sendall(b"POWER: Enter the exponent: ")
                        inp_n2 = conn.recv(1024)
                        n1 = self.integer_check(conn, inp_n1)
                        n2 = self.integer_check(conn, inp_n2)
                        if func_op != -1 and n1 != -1 and n2 != -1:
                            ans = self.calc.power(n1, n2)
                            conn.sendall(f"\n{bcolors.OKGREEN}OUTPUT: ".encode() + str(ans).encode())
                        else:
                            continue
                    elif func_op == 6:
                        logging.info("[CLIENT] EXIT")
                        conn.sendall(b"EXITING\n")
                        break
                    else:
                        logging.error("[CLIENT] Chose an invalid menu object")
                        conn.sendall(f"{bcolors.FAIL}Choose a valid number between 1-6\n".encode())
                else:
                    continue

                conn.sendall(b"\n________________________________________\n\n")
                
        conn.sendall(b"Bye! \n")
        conn.close()
        print('Connection ' + ip + ':' + port + " ended")

# conn.sendall()
# conn.recv(1024)