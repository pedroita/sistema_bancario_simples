from Pessoa import Cliente
class ClientePJ(Cliente):
    def __init__(self,nome,endereco,cnpj,):
        super().__init__(nome,endereco)
        self__cnpj = cnpj
        