from Service.criar_conta_usecase import CriarContaUseCase
from Service.depositar_usecase import DepositarUseCase
from Service.sacar_usecase import SacarUseCase
from Service.historico_usecase import HistoricoUseCase
from Service.poupanca_usecase import PoupancaUseCase

class ContaController:
    def __init__(self, view, repository):
        self.view = view
        self.repository = repository

        self.criar_conta_usecase = CriarContaUseCase(repository)
        self.depositar_usecase = DepositarUseCase(repository)
        self.sacar_usecase = SacarUseCase(repository)
        self.historico_usecase = HistoricoUseCase()
        self.poupanca_usecase = PoupancaUseCase(repository)

        self.proximo_numero = 1
        self.conta_atual = None
        self.valor = None

    def criar_conta(self):
        dados = self.view.obter_dados()

        nome = dados["nome"].strip()
        cpf = dados["cpf"].strip()
        saldo_texto = dados["saldo_inicial"].strip()

        if not nome or not cpf or not saldo_texto:
            self.view.mostrar_erro("Preencha todos os campos.")
            return

        try:
            saldo_inicial = float(saldo_texto.replace(",", "."))
        except ValueError:
            self.view.mostrar_erro("Saldo inicial inválido.")
            return

        if saldo_inicial < 0:
            self.view.mostrar_erro("O saldo inicial não pode ser negativo.")
            return

        conta = self.criar_conta_usecase.executar(
            nome=nome,
            cpf=cpf,
            saldo_inicial=saldo_inicial,
            numero=self.proximo_numero
        )

        self.conta_atual = conta
        self.proximo_numero += 1

        self.view.mostrar_conta(conta)

    def depositar(self):
        if self.conta_atual is None:
            self.view.mostrar_erro("Crie uma conta primeiro.")
            return

        valor_texto = self.view.obter_valor().strip()

        if not valor_texto:
            self.view.mostrar_erro("Digite um valor para depósito.")
            return

        try:
            valor = float(valor_texto.replace(",", "."))
        except ValueError:
            self.view.mostrar_erro("Valor de depósito inválido.")
            return

        sucesso, mensagem = self.depositar_usecase.executar(self.conta_atual, valor)

        if sucesso:
            self.view.mostrar_mensagem(mensagem)
            self.view.mostrar_conta(self.conta_atual)
        else:
            self.view.mostrar_erro(mensagem)

    def sacar(self):
        if self.conta_atual is None:
            self.view.mostrar_erro("Crie uma conta primeiro.")
            return

        valor_texto = self.view.obter_valor().strip()

        if not valor_texto:
            self.view.mostrar_erro("Digite um valor para saque.")
            return

        try:
            valor = float(valor_texto.replace(",", "."))
        except ValueError:
            self.view.mostrar_erro("Valor de saque inválido.")
            return

        sucesso, mensagem = self.sacar_usecase.executar(self.conta_atual, valor)

        if sucesso:
            self.view.mostrar_mensagem(mensagem)
            self.view.mostrar_conta(self.conta_atual)
        else:
            self.view.mostrar_erro(mensagem)

    def ver_historico(self):
        if self.conta_atual is None:
            self.view.mostrar_erro("Crie uma conta primeiro.")
            return

        historico = self.historico_usecase.executar(self.conta_atual)
        self.view.mostrar_historico(historico)

    def investimento(self):
        if valor <= 0:
            self.view.mostrar_erro("Valor invalido")
            return

        if valor > self._saldoinvestido:
            return False

        self._saldo += valor
        return True
