import unittest
from main import TesteSoma

class TesteSomaTeste(unittest.TestCase):

    def teste_2_numeros(self):
        cc = TesteSoma()
        self.assertEqual(cc.testa_soma(), 4), 'A soma dos números não é 6'


if __name__ == '__main__':
    unittest.main()