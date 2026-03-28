class DepositarUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, conta, valor):
        if valor <= 0:
            return False, "O valor do depósito deve ser maior que zero."

        sucesso = conta.depositar(valor)

        if sucesso:
            conta.historico.adicionar_transacao("Depósito", valor)
            self.repository.salvar(conta)
            return True, "Depósito realizado com sucesso."

        return False, "Não foi possível realizar o depósito."