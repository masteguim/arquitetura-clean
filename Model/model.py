from datetime import date


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self._transacoes.append({
            "tipo": tipo,
            "valor": valor
        })

    def listar(self):
        return self._transacoes


class Conta:
    def __init__(self, cliente, numero: int, agencia: str):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor: float):
        if valor <= 0:
            return False

        if valor > self._saldo:
            return False

        self._saldo -= valor
        return True

    def depositar(self, valor: float):
        if valor <= 0:
            return False

        self._saldo += valor
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, agencia: str, limite: float, limite_saques: int):
        super().__init__(cliente, numero, agencia)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques


class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento