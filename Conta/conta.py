from PessoaFisica import ClientePF
from PessoaJuridica import ClientePJ
     
class Conta:
    __quantidade = 0
    @classmethod
    def adicionar_conta(cls):
        cls.__quantidade+=1
    @classmethod
    def quantidade(cls):
        return cls.__quantidade
    
    def __init__(self,numero, cliente):
        self.adicionar_conta()
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = 0.0
    
    def depositar (self, valor):
        self.__saldo += valor
    def saldo (self):
        return self.__saldo
    def sacar(self,valor):
        if self.__saldo>=valor:
            self.__saldo-= valor
            return True
        return False
    def transferir(self,destino,valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False
    def imprime(self):
        print('Conta:', str(self.__numero),'\nSaldo: ' , str(self.__saldo))
        self.__cliente.imprime()

cliente = ClientePF('Ana', 'rua da ostras', 'xxx.xxx.xx-xxx', '2023-05-20')
conta1 = Conta(555,cliente)
cliente2 = ClientePJ('LUiz', 'Rua três', 'xxx-xxx-x-x-x-x')
conta2 = Conta(9999, cliente2)
print("Contas criadas", Conta.quantidade())
conta2.depositar(500.00)
print("Saldo atual")
print('Conta 1:', conta1.saldo())
print ("Saldo atual")
print('Conta 2:', conta2.saldo())

conta2.transferir(conta1,200.00)
print("Saldo após transferencia")
conta1.imprime()
conta2.imprime()
print("Conta 1:", conta1.saldo())
print("Conta 2:", conta2.saldo())