import logging
import math

class Calculator():
    def __init__(self):
        pass

    def log(self, n):
        logging.info("Function [COMMON LOGARITHM] "+str(n))
        if n > 0:
            return math.log10(n)
        else:
            logging.error("Negative value for log "+str(n))
            return "Undefined"
    
    def ln(self, n):
        logging.info("Function [NATURAL LOGARITHM] "+str(n))
        if n > 0:
            return math.log(n)
        else:
            logging.error("Negative value for ln"+str(n))
            return "Undefined"
    
    def squrt(self, n):
        logging.info("Function [SQUARE ROOT] "+str(n))
        if n >= 0:
            return n**(1/2)
        else:
            logging.error("Negative value for square root "+str(n))
            return "Undefined"
    
    def add(self, n1, n2):
        logging.info("Operation [ADDITION] "+str(n1)+" "+str(n2))
        return n1+n2
    
    def multiply(self, n1, n2):
        logging.info("Operation [MULTIPLICATION] "+str(n1)+" "+str(n2))
        return n1*n2
    
    def power(self, n1, n2):
        logging.info("Operation [POWER] "+str(n1)+" "+str(n2))
        return n1**n2
        
    def subtract(self, n1, n2):
        logging.info("Operation [SUBTRACTION] "+str(n1)+" "+str(n2))
        return n1-n2
    
    def divide(self, n1, n2):
        logging.info("Operation [DIVISION] "+str(n1)+" "+str(n2))
        return n1/n2
    
    def percent(self, n1, n2):
        logging.info("Operation [PERCENTAGE] "+str(n1)+" "+str(n2))
        return n1*(self, n2/100)
    
    def factorial(self, n):
        logging.info("Function [FACTORIAL]"+str(n))
        if int(n) == n:
            if(n == 0) :
                return 1
            
            elif(n > 0) :
                return n * self.factorial(n-1)
            
            else :
                logging.error("Negative value for factorial "+str(n))
                return "Undefined"
        else :
            logging.error("Decimal value for factorial "+str(n))
            return "Undefined"