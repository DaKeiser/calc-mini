from calculator import *
import unittest, socket, math, logging

from calculator.calculator import Calculator

class SquareRootTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_sqrt_7(self):
        # print("Check the sqrt with 0")
        self.assertEqual(self.calc.squrt(0), 0)

    def test_sqrt_0(self):
        # print("Check the sqrt")
        self.assertEqual(self.calc.squrt(1), 1)

    def test_sqrt_1(self):
        # print("Check the sqrt")
        self.assertEqual(self.calc.squrt(2), 1.4142135623730951)

    def test_sqrt_2(self):
        # print("Check the sqrt")
        self.assertEqual(self.calc.squrt(4), 2)

    def test_sqrt_3(self):
        # print("Check the sqrt")
        self.assertEqual(self.calc.squrt(10), 3.1622776601683795)

    def test_sqrt_4(self):
        # print("Check the sqrt")
        self.assertEqual(self.calc.squrt(-10), "Undefined")

    def test_sqrt_5(self):
        # print("[TRUE NEGATIVE] Check the sqrt")
        self.assertNotEqual(self.calc.squrt(10), -1)

    def test_sqrt_6(self):
        # print("[DECIMAL]Check the sqrt")
        self.assertEqual(self.calc.squrt(7.1), 2.6645825188948455)


class Log10Tests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_log_0(self):
        # print("Check the log with 0")
        self.assertEqual(self.calc.log(0), "Undefined")

    def test_log_1(self):
        # print("Check the log")
        self.assertEqual(self.calc.log(1), 0)

    def test_log_2(self):
        # print("Check the log")
        self.assertEqual(self.calc.log(2), 0.3010299956639812)

    def test_log_3(self):
        # print("Check the log")
        self.assertEqual(self.calc.log(10), 1)

    def test_log_4(self):
        # print("[TRUE NEGATIVE] Check the log")
        self.assertNotEqual(self.calc.log(10), -1)

    def test_log_5(self):
        # print("[DECIMAL]Check the log")
        self.assertEqual(self.calc.log(7.1), 0.8512583487190752)

class LogTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_ln_0(self):
        # print("Check the ln with 0")
        self.assertEqual(self.calc.ln(0), "Undefined")

    def test_ln_1(self):
        # print("Check the ln")
        self.assertEqual(self.calc.ln(1), 0)

    def test_ln_2(self):
        # print("Check the ln")
        self.assertEqual(self.calc.ln(2), 0.6931471805599453)

    def test_ln_3(self):
        # print("[TRUE NEGATIVE] Check the ln")
        self.assertNotEqual(self.calc.ln(math.e), -1)

    def test_ln_4(self):
        # print("[DECIMAL]Check the ln")
        self.assertEqual(self.calc.ln(7.1), 1.9600947840472698)

class FactorialTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_fact_0(self):
        # print("Check the factorial")
        self.assertEqual(self.calc.factorial(7), 5040)

    def test_fact_1(self):
        # print("Check the factorial")
        self.assertEqual(self.calc.factorial(1), 1)

    def test_fact_2(self):
        # print("Check the factorial")
        self.assertEqual(self.calc.factorial(2), 2)

    def test_fact_3(self):
        # print("[TRUE NEGATIVE] Check the factorial")
        self.assertNotEqual(self.calc.factorial(7), -4)

    def test_fact_4(self):
        # print("[DECIMAL]Check the factorial")
        self.assertEqual(self.calc.factorial(7.1), "Undefined")

class PowerTests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_power_0(self):
        # print("Check the power with 0")
        self.assertEqual(self.calc.power(0, 0), 1)

    def test_power_1(self):
        # print("Check the power with 0")
        self.assertEqual(self.calc.power(10, 0), 1)

    def test_power_2(self):
        # print("Check the power")
        self.assertEqual(self.calc.power(2, 4), 16)

    def test_power_3(self):
        # print("[TRUE NEGATIVE] Check the power")
        self.assertNotEqual(self.calc.power(2, 5), -10)

    def test_power_4(self):
        # print("[DECIMAL]Check the power")
        self.assertEqual(self.calc.power(2, 0.5), 1.4142135623730951)

    def test_power_5(self):
        # print("Check the power with negative exponenet")
        self.assertEqual(self.calc.power(2, -4), 0.0625)

    def test_power_6(self):
        # print("Check the negative value's power")
        self.assertEqual(self.calc.power(-2, -4), 0.0625)
    
# class SocketConnectTests(unittest.TestCase):
#     def setUp(self):
#         client_socket = socket(AF_INET, SOCK_STREAM)
#         client_socket.connect(('', port_number))

#     def tearDown(self):
#         client_socket.close()

#     def test_1(self):
#         client_socket.send('message1'.encode())
#         self.self.assertEqual(client_socket.recv(1024).decode(), 'reply1')

#     def test_2(self):
#         client_socket.send('message2'.encode())
#         self.self.assertEqual(client_socket.recv(1024).decode(), 'reply2')

if __name__ == "__main__":
    unittest.main()