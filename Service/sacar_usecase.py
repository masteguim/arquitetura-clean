class SacarUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, conta, valor):
        if valor <= 0:
            return False, "O valor do saque deve ser maior que zero."

        sucesso = conta.sacar(valor)

        if sucesso:
            conta.historico.adicionar_transacao("Saque", valor)
            self.repository.salvar(conta)
            return True, "Saque realizado com sucesso."

        return False, "Saldo insuficiente para saque."