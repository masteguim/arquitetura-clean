class HistoricoUseCase:
    def executar(self, conta):
        return conta.historico.listar()