from .simple_report import SimpleReport


class CompleteReport:
    def get_stock(products):
        companies = {}
        for product in products:
            if product["nome_da_empresa"] not in companies:
                companies[product["nome_da_empresa"]] = 1
            else:
                companies[product["nome_da_empresa"]] += 1

        frase = ""
        for company, quantity in companies.items():
            frase += f"- {company}: {quantity}\n"
        complete = (
            f"Produtos estocados por empresa:\n{frase}"
            )
        return complete

    def generate(products):
        simple = SimpleReport.generate(products)

        complete = CompleteReport.get_stock(products)

        return simple + "\n" + complete
