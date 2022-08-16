class Product:
    def __init__(
        self,
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    ):
        self.id = id
        self.nome_do_produto = nome_do_produto
        self.nome_da_empresa = nome_da_empresa
        self.data_de_fabricacao = str(data_de_fabricacao)
        self.data_de_validade = str(data_de_validade)
        self.numero_de_serie = numero_de_serie
        self.instrucoes_de_armazenamento = instrucoes_de_armazenamento

    def __repr__(self):
        return (
            f"O produto {self.nome_do_produto}"
            f" fabricado em {self.data_de_fabricacao}"
            f" por {self.nome_da_empresa} com validade"
            f" até {self.data_de_validade}"
            f" precisa ser armazenado {self.instrucoes_de_armazenamento}."
        )


print(Product(
    1, "Nicotine Polacrilex", "Target Corporation",
    "2021-02-18", "2023-09-17",
    "CR25 1551 4467 2549 4402 1", "instrucao 1")
)
