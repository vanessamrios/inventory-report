import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    def read(path):
        products = []
        with open(path) as file:
            content = csv.DictReader(file)
            for line in content:
                products.append(line)
        return products

    def import_data(path, type):

        content = Inventory.read(path)

        if type == "simples":
            return SimpleReport.generate(content)

        if type == "completo":
            return CompleteReport.generate(content)
