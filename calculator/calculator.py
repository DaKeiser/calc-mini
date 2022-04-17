import logging
import math

class Calculator():
    def __init__(self):
        pass

    def log(self, n):
        logging.info("[CALCULATOR] [COMMON LOGARITHM] "+str(n))
        if n > 0:
            return math.log10(n)
        else:
            logging.error("[CALCULATOR] [COMMON LOGARITHM] Negative value for log "+str(n))
            return "Undefined"
    
    def ln(self, n):
        logging.info("[CALCULATOR] [NATURAL LOGARITHM] "+str(n))
        if n > 0:
            return math.log(n)
        else:
            logging.error("[CALCULATOR] [NATURAL LOGARITHM] Negative value for ln "+str(n))
            return "Undefined"
    
    def squrt(self, n):
        logging.info("[CALCULATOR] [SQUARE ROOT] "+str(n))
        if n >= 0:
            return n**(1/2)
        else:
            logging.error("[CALCULATOR] [SQUARE ROOT] Negative value for square root "+str(n))
            return "Undefined"
    
    def add(self, n1, n2):
        logging.info("[CALCULATOR] [ADDITION] "+str(n1)+" "+str(n2))
        return n1+n2
    
    def multiply(self, n1, n2):
        logging.info("[CALCULATOR] [MULTIPLICATION] "+str(n1)+" "+str(n2))
        return n1*n2
    
    def power(self, n1, n2):
        logging.info("[CALCULATOR] [POWER] "+str(n1)+" "+str(n2))
        return n1**n2
        
    def subtract(self, n1, n2):
        logging.info("[CALCULATOR] [SUBTRACTION] "+str(n1)+" "+str(n2))
        return n1-n2
    
    def divide(self, n1, n2):
        logging.info("[CALCULATOR] [DIVISION] "+str(n1)+" "+str(n2))
        return n1/n2
    
    def percent(self, n1, n2):
        logging.info("[CALCULATOR] [PERCENTAGE] "+str(n1)+" "+str(n2))
        return n1*(self, n2/100)
    
    def factorial(self, n):
        logging.info("[CALCULATOR] [FACTORIAL] "+str(n))
        if int(n) == n:
            if n >= 0:
                return math.factorial(n)            
            else :
                logging.error("[CALCULATOR] [FACTORIAL] Negative value for factorial "+str(n))
                return "Undefined"
        else :
            logging.error("[CALCULATOR] [FACTORIAL] Decimal value for factorial "+str(n))
            return "Undefined"
