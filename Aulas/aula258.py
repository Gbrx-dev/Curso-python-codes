"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod



# PESSOA (ABSTRAÇÃO)

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade



# CLIENTE (HERANÇA)

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta = None  # agregação



# CONTA (ABSTRAÇÃO)
class Conta(ABC):
    def __init__(self, agencia: int, numero: int, saldo: float = 0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor inválido para depósito")
            return

        self.saldo += valor
        print(f"Depósito realizado. Saldo atual: {self.saldo}")

    @abstractmethod
    def sacar(self, valor: float):
        pass



# CONTA POUPANÇA

class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return False

        self.saldo -= valor
        print(f"Saque realizado. Saldo atual: {self.saldo}")
        return True



# CONTA CORRENTE

class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        limite_total = self.saldo + self.limite

        if valor > limite_total:
            print("Saldo + limite insuficiente")
            return False

        self.saldo -= valor
        print(f"Saque realizado. Saldo atual: {self.saldo}")
        return True



# BANCO (AGREGAÇÃO + REGRAS)

class Banco:
    def __init__(self, agencias: list[int]):
        self.agencias = agencias
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def autenticar(self, cliente: Cliente):
        if cliente not in self.clientes:
            print("Cliente não pertence ao banco")
            return False

        if cliente.conta not in self.contas:
            print("Conta não pertence ao banco")
            return False

        if cliente.conta.agencia not in self.agencias:
            print("Agência inválida")
            return False

        return True

    def sacar(self, cliente: Cliente, valor: float):
        if not self.autenticar(cliente):
            print("Falha na autenticação")
            return

        cliente.conta.sacar(valor)

# Criando banco
banco = Banco(agencias=[1111, 2222])

# Criando cliente
cliente1 = Cliente("Gabriel", 25)

# Criando conta
conta1 = ContaCorrente(1111, 12345, saldo=1000, limite=500)

# Ligando cliente à conta
cliente1.conta = conta1

# Adicionando ao banco
banco.adicionar_cliente(cliente1)
banco.adicionar_conta(conta1)

# Testes
banco.sacar(cliente1, 1200)  # usa saldo + limite
banco.sacar(cliente1, 500)   # pode falhar dependendo do saldo