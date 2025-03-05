
### `README.md`  

```md
# Sistema de Controle de Estoque  

Este é um projeto simples de **Controle de Estoque** desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **SQLite** para armazenamento de dados. O principal objetivo deste projeto foi **praticar a construção de interfaces gráficas, a criação de um crud e o uso de bancos de dados SQLite**.

## 🚀 Funcionalidades  

- 📦 **Adicionar produtos** ao estoque  
- 📜 **Listar produtos** cadastrados  
- ✏ **Editar produtos** existentes  
- ❌ **Excluir produtos** do banco de dados  

## 🛠 Tecnologias Utilizadas  

- **Python 3**  
- **Tkinter (com ttkbootstrap para estilização da interface)**  
- **SQLite (Banco de Dados embutido)**  

## 📂 Estrutura do Projeto  

```
sistema-de-controle-de-estoque/
│── executavel/             # Pasta contendo o executável do sistema
│── banco.py                # Gerenciamento do banco de dados SQLite
│── interface.py            # Interface gráfica do sistema (Tkinter)
│── main.py                 # Arquivo principal para execução do programa
```

## 🖥 Como Executar  

1. Certifique-se de ter o **Python 3** instalado em seu sistema.  
2. Instale o **ttkbootstrap** (caso ainda não tenha):  
   ```bash
   pip install ttkbootstrap
   ```
3. Execute o arquivo `main.py`:  
   ```bash
   python main.py
   ```

## 🔧 Possíveis Melhorias  

Aqui estão algumas melhorias que podem ser feitas no projeto:  

### 📌 Banco de Dados (`banco.py`)  
 - Implementar um sistema de **pesquisa e filtros** para encontrar produtos mais rapidamente.  

### 🎨 Interface Gráfica (`interface.py`)  

#### **Gerais**  
- Implementar um **tema dinâmico**, permitindo ao usuário escolher diferentes estilos.  
- Tornar a janela **responsiva**, adaptando-se a diferentes tamanhos de tela.  

#### **Separação dos Métodos**  

| Método                | Função |
|-----------------------|--------|
| `validar_entrada_float` | Valida se o preço é um número válido. |
| `validar_quantidade` | Valida se a quantidade é um número inteiro. |
| `coletar_dados_produto` | Coleta os dados inseridos nos campos de entrada. |
| `limpar_entradas` | Limpa os campos de entrada após a inserção ou edição. |
| `adicionar_produto` | Adiciona um novo produto ao banco de dados. |
| `listar_produtos` | Lista os produtos cadastrados no estoque. |
| `editar_produto` | Edita os detalhes de um produto selecionado. |
| `excluir_produtos` | Exclui um produto selecionado do estoque. |

