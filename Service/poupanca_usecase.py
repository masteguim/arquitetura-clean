class PoupancaUseCase:
    def __init__(self, repository):
        self.repository = repository
        self._investimento = 0
        self._Poupanca =  []

        def Poupanca(self, contapoupanca, valorpoupanca, investimento):
            if valor < 0 or investimento == 0:
                return False, "O valor inserido não é adequado, deve ser maior do que zero."

            sucesso = contapoupanca.saldo(valorpoupanca)
            if sucesso:
                contapoupanca.saldo.adicionar_investimento("valor desejado", investimento)
                self.repository.saldo(investimento)
                return True, "Investimento adicionado com sucesso."

            return False, "Não foi possivel adicionar."
