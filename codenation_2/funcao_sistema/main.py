
class FuncaoSistema:

    def login(self, email, senha):
         
        email_teste = 'juliano.silva@wavecode.com.br'
        senha_teste = 'teste'

        if email_teste == email and senha_teste == senha:
            return True
        return False