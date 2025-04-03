import unittest
from main import sumar, restar, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 4), 7)
        self.assertEqual(sumar(-1, 5), 4)

    def test_restar(self):
        self.assertEqual(restar(10, 3), 7)
        self.assertEqual(restar(5, 8), -3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 5), 15)
        self.assertEqual(multiplicar(0, 100), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(7, -1), -7)
        self.assertEqual(dividir(0, 1), 0)
        self.assertEqual(dividir(5, 0), "Error: No se puede dividir por cero")


if __name__ == '__main__':
    unittest.main()
