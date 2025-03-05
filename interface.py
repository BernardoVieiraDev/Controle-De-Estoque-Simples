import ttkbootstrap as ttk
from banco import *

class InterfaceEstoque:
    def __init__(self):
        self.bd = BancoDeDados()

        self.root = ttk.Window(themename="superhero")
        self.root.title("Sistema De Controle De Estoque")
        self.root.geometry("800x500")

        self.label_nome = ttk.Label(self.root, text="Nome do produto:")
        self.label_nome.place(x=10, y=10)

        self.entrada_nome = ttk.Entry(self.root)
        self.entrada_nome.place(x=180, y=10)

        self.label_preco = ttk.Label(self.root, text="Preço:")
        self.label_preco.place(x=10, y=50)

        self.entrada_preco = ttk.Entry(self.root)
        self.entrada_preco.place(x=180, y=50)

        self.label_quantidade = ttk.Label(self.root, text="Quantidade disponível:")
        self.label_quantidade.place(x=10, y=90)

        self.entrada_quantidade = ttk.Entry(self.root)
        self.entrada_quantidade.place(x=180, y=90)

        self.label_id_categoria = ttk.Label(self.root, text="Categoria:")
        self.label_id_categoria.place(x=10, y=130)

        self.combo_categoria = ttk.Combobox(self.root, values=["Smartphones", "Computadores e Laptops", "Periféricos", "Câmeras e Filmadoras", 
                                                              "Acessórios para Smartphones", "Placas de Vídeo", "Armazenamento", "Redes e Wi-Fi", 
                                                              "Gaming", "Eletrônicos de Áudio"])
        self.combo_categoria.place(x=180, y=130)

        self.label_id_fornecedor = ttk.Label(self.root, text="Fornecedor:")
        self.label_id_fornecedor.place(x=10, y=170)

        self.combo_fornecedor = ttk.Combobox(self.root, values=["Dell", "Logitech", "Samsung", "Apple", "Sony", "HP", "Asus", "Acer", "Razer", "Corsair"])
        self.combo_fornecedor.place(x=180, y=170)

        self.btn_adicionar = ttk.Button(self.root, text="Adicionar Produto", command=self.adicionar_produto)
        self.btn_adicionar.place(x=10, y=210)

        self.btn_listar = ttk.Button(self.root, text="Listar Produtos", command=self.listar_produtos)
        self.btn_listar.place(x=140, y=210)

        self.btn_editar = ttk.Button(self.root, text="Editar Produto", command=self.editar_produto)
        self.btn_editar.place(x=250, y=210)

        self.btn_excluir = ttk.Button(self.root, text="Excluir Produtos", command=self.excluir_produtos)
        self.btn_excluir.place(x=360, y=210)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nome", "Preço", "Quantidade", "Fornecedor", "Categoria"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preço", text="Preço")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Fornecedor", text="Fornecedor")
        self.tree.heading("Categoria", text="Categoria")

        self.tree.column("ID", width=50, anchor="center")  
        self.tree.column("Nome", width=200, anchor="center")   
        self.tree.column("Preço", width=100, anchor="center")   
        self.tree.column("Quantidade", width=100, anchor="center")  
        self.tree.column("Fornecedor", width=150, anchor="center")  
        self.tree.column("Categoria", width=150, anchor="center")


        self.tree.column("ID", stretch=False)
        self.tree.column("Nome", stretch=False)
        self.tree.column("Preço", stretch=False)
        self.tree.column("Quantidade", stretch=False)
        self.tree.column("Fornecedor", stretch=False)
        self.tree.column("Categoria", stretch=False)

        self.tree.place(x=10, y=265)

        self.root.mainloop()

    def validar_entrada_float(self, valor):
        try:
            float(valor)
            return True
        except ValueError:
            messagebox.showwarning("Entrada inválida", "O valor do preço deve ser numérico. Por favor, use ponto (.) e não vírgula (,) para separar as casas decimais.")
            return False
        
    def validar_quantidade(self, valor):
        if valor.isdigit():
            return True
        else:
            messagebox.showwarning("Entrada inválida", "O valor de quantidade deve ser numérico e inteiro.")
            return False  

    def coletar_dados_produto(self):
        nome = self.entrada_nome.get()
        preco = self.entrada_preco.get()
        quantidade = self.entrada_quantidade.get()
        fornecedor = self.combo_fornecedor.get()
        categoria = self.combo_categoria.get()
        return nome, preco, quantidade, fornecedor, categoria   

    def limpar_entradas(self):
        self.entrada_nome.delete(0, ttk.END)
        self.entrada_preco.delete(0, ttk.END)
        self.entrada_quantidade.delete(0, ttk.END)
        self.combo_fornecedor.set('')
        self.combo_categoria.set('')

    def adicionar_produto(self):
        nome, preco, quantidade, fornecedor, categoria = self.coletar_dados_produto()

        if not all([nome, preco, quantidade, fornecedor, categoria]):
            messagebox.showwarning("Entrada inválida", "Preencha todos os campos.")
            return

        if not self.validar_entrada_float(preco):
            return
        if not self.validar_quantidade(quantidade):
            return
        
        if self.bd.verificar_existencia(nome, fornecedor):
            messagebox.showwarning("Produto já existente", "Este produto já foi adicionado com o mesmo fornecedor.")
            return

        preco = float(preco)
        quantidade = int(quantidade)

        self.bd.adicionar_produto(nome, preco, quantidade, fornecedor, categoria)

        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        self.listar_produtos()
        self.limpar_entradas()

    def listar_produtos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        produtos = self.bd.listar_produtos()
        for produto in produtos:
            self.tree.insert("", "end", values=produto)

    def editar_produto(self):
        selected_item = self.tree.selection()
        if selected_item:
            produto_id = self.tree.item(selected_item[0])["values"][0]
            produto = self.bd.executar_comando("SELECT * FROM produtos WHERE id = ?", (produto_id,))

            if produto:

                nome, preco, quantidade, fornecedor, categoria = self.coletar_dados_produto()
 
                if not all([nome, preco, quantidade, fornecedor, categoria]):
                    messagebox.showwarning("Entrada inválida", "Preencha todos os campos.")
                    return

                if not self.validar_entrada_float(preco):
                    return
                if not self.validar_quantidade(quantidade):
                    return

                preco = float(preco)
                quantidade = int(quantidade)

                self.bd.editar_produto(produto_id, nome, preco, quantidade, fornecedor, categoria)

                messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
                self.listar_produtos()
            else:
                messagebox.showwarning("Seleção", "Por favor, selecione um produto para editar.")
    
    
    def excluir_produtos(self):
        selected_item = self.tree.selection()
        if selected_item:
            produto_id = self.tree.item(selected_item[0])['values'][0]
            confirmacao = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir este produto?")
            if confirmacao:    
                self.bd.excluir_produto(produto_id)
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
                self.listar_produtos()
        else:
            messagebox.showwarning("Seleção", "Por favor, selecione um produto para excluir.")