from datetime import date
import statistics


class SimpleReport:

    def find_oldest_manufacturing(products):
        dates = []
        for product in products:
            dates.append(date.fromisoformat(product["data_de_fabricacao"]))
        return min(dates)

    def find_expiration_date(products):
        dates = []
        for product in products:
            expiration_date = date.fromisoformat(product["data_de_validade"])
            if (expiration_date > date.today()):
                dates.append(expiration_date)
        return min(dates)

    def generate(products):
        manufacturing = SimpleReport.find_oldest_manufacturing(products)

        expiration = SimpleReport.find_expiration_date(products)

        company = statistics.mode(
            product["nome_da_empresa"] for product in products)

        report = (
            f"Data de fabricação mais antiga: {manufacturing}\n"
            f"Data de validade mais próxima: {expiration}\n"
            f"Empresa com mais produtos: {company}"
            )

        return report
