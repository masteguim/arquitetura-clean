class AplicarRendimentoUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, conta):
        sucesso = conta.aplicar_rendimento()

        if sucesso:
            self.repository.salvar(conta)
            return True, "Rendimento aplicado com sucesso."

        return False, "Não foi possível aplicar rendimento."