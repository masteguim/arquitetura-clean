import tkinter as tk
from tkinter import messagebox


class Interfaceconta:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x350')
        self.root.title("CONTA BANCÁRIA")
        self.root.resizable(False, False)


class ContaView(Interfaceconta):
    def __init__(self, root):
        super().__init__(root)

        self.controller = None

        tk.Label(self.root, text="Nome").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.ent_nome = tk.Entry(self.root, width=30)
        self.ent_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="CPF").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.ent_cpf = tk.Entry(self.root, width=30)
        self.ent_cpf.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Saldo Inicial R$:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.ent_saldo_inicial = tk.Entry(self.root, width=30)
        self.ent_saldo_inicial.grid(row=2, column=1, padx=10, pady=10)

        self.btn_criar = tk.Button(self.root, text="Criar Conta", command=self.ao_clicar_criar)
        self.btn_criar.grid(row=3, column=0, columnspan=2, pady=15)

        tk.Label(self.root, text="Valor").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.ent_valor = tk.Entry(self.root, width=30)
        self.ent_valor.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Depositar", command=self.ao_clicar_depositar).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Sacar", command=self.ao_clicar_sacar).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Histórico", command=self.ao_clicar_historico).grid(row=6, column=0, columnspan=2, pady=10)

    def set_controller(self, controller):
        self.controller = controller

    def ao_clicar_criar(self):
        if self.controller:
            self.controller.criar_conta()

    def ao_clicar_depositar(self):
        if self.controller:
            self.controller.depositar()

    def ao_clicar_sacar(self):
        if self.controller:
            self.controller.sacar()

    def ao_clicar_historico(self):
        if self.controller:
            self.controller.ver_historico()

    def obter_dados(self):
        return {
            "nome": self.ent_nome.get(),
            "cpf": self.ent_cpf.get(),
            "saldo_inicial": self.ent_saldo_inicial.get()
        }

    def obter_valor(self):
        return self.ent_valor.get()

    def mostrar_conta(self, conta):
        relatorio = (
            f"Nome: {conta.cliente.nome}\n"
            f"CPF: {conta.cliente.cpf}\n"
            f"Agência: {conta.agencia}\n"
            f"Número: {conta.numero}\n"
            f"Saldo: R$ {conta.saldo:.2f}"
        )
        messagebox.showinfo("Conta Criada", relatorio)

    def mostrar_mensagem(self, msg):
        messagebox.showinfo("Info", msg)

    def mostrar_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)

    def mostrar_historico(self, historico):
        texto = ""
        for t in historico:
            texto += f"{t['tipo']}: R$ {t['valor']:.2f}\n"

        messagebox.showinfo("Histórico", texto if texto else "Sem transações.")

if __name__ == '__main__':
    class ControllerFake:
        def criar_conta(self):
            print("Criar conta clicado")

        def depositar(self):
            print("Depositar clicado")

        def sacar(self):
            print("Sacar clicado")

        def ver_historico(self):
            print("Histórico clicado")

    root = tk.Tk()
    view = ContaView(root)
    view.set_controller(ControllerFake())
    root.mainloop()