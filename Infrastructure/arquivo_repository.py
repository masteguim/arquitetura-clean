from Interface.conta_repository import IContaRepository


class ArquivoContaRepository(IContaRepository):
    def __init__(self, caminho="contas.txt"):
        self.caminho = caminho

    def salvar(self, conta):
        with open(self.caminho, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Conta: {conta.numero}\n")
            arquivo.write(f"Nome: {conta.cliente.nome}\n")
            arquivo.write(f"CPF: {conta.cliente.cpf}\n")
            arquivo.write(f"Agencia: {conta.agencia}\n")
            arquivo.write(f"Saldo: {conta.saldo}\n")
            arquivo.write("Historico:\n")
            arquivo.write(f"Investimento: {conta.investimento}\n")

            for transacao in conta.historico.listar():
                arquivo.write(f"- {transacao['tipo']}: {transacao['valor']}\n")

            arquivo.write("---\n")

    def buscar(self, numero):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            bloco = []
            for linha in linhas:
                linha = linha.strip()

                if linha == "---":
                    if bloco:
                        numero_linha = bloco[0].replace("Conta: ", "")
                        if numero_linha == str(numero):
                            return bloco
                    bloco = []
                else:
                    bloco.append(linha)

        except FileNotFoundError:
            return None

        return None