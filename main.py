import tkinter as tk
from View.view import ContaView
from Controller.controller import ContaController
from Infrastructure.arquivo_repository import ArquivoContaRepository


root = tk.Tk()

view = ContaView(root)
repository = ArquivoContaRepository()
controller = ContaController(view, repository)

view.set_controller(controller)

root.mainloop()