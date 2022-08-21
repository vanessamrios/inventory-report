import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    def read_csv(path):
        products = []
        with open(path) as file:
            content = csv.DictReader(file)
            for line in content:
                products.append(line)
        return products

    def read_json(path):
        with open(path) as file:
            content = file.read()
            products = json.loads(content)
        return products

    def import_data(path, type):

        if path.endswith(".csv"):
            content = Inventory.read_csv(path)
        if path.endswith(".json"):
            content = Inventory.read_json(path)

        if type == "simples":
            return SimpleReport.generate(content)

        if type == "completo":
            return CompleteReport.generate(content)
