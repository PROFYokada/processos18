class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__preco = preco

    # Getter e Setter para titulo
    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    # Getter e Setter para autor
    def get_autor(self):
        return self.__autor

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    # Getter e Setter para ano_publicacao
    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def set_ano_publicacao(self, novo_ano):
        self.__ano_publicacao = novo_ano

    # Getter e Setter para preco
    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

# Criando instância da classe Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 120.0)

# Testando getters
print(livro1.get_titulo())           # O Senhor dos Anéis
print(livro1.get_autor())            # J.R.R. Tolkien
print(livro1.get_ano_publicacao())   # 1954
print(livro1.get_preco())            # 120.0

# Testando setters
livro1.set_titulo("Harry Potter e a Pedra Filosofal")
livro1.set_autor("J.K. Rowling")
livro1.set_ano_publicacao(1997)
livro1.set_preco(100.0)

# Verificando alterações
print(livro1.get_titulo())           # O Hobbit
print(livro1.get_autor())            # J.R.R. Tolkien Jr.
print(livro1.get_ano_publicacao())   # 1937
print(livro1.get_preco())            # 90.0

FIZ MERDA 
