class Cliente:
    def __init__(self, nome, endereco) :
        self.__nome = nome
        self.__endereco = endereco
    def imprime(self):
        print('Cliente: ', self.__nome, '(' , type(self) , ')' ,'\nEndereco: ', self.__endereco )