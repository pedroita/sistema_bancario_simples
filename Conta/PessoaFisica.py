from Pessoa import Cliente
class ClientePF(Cliente):
    def __init__(self,nome,endereco,cpf,nascimento):
        super().__init__(nome,endereco)
        self__cpf = cpf
        self.__nascimento= nascimento
