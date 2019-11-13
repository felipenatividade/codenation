from main import FuncaoSistema
import unittest


class TesteFuncaoSistema(unittest.TestCase):
    
    def test_login(self):
        instancia_classe = FuncaoSistema()
        self.assertEqual(instancia_classe.login('juliano.silva@wavecode.com.br', 'teste'), True)


if __name__ == '__main__':
    unittest.main()