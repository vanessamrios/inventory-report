import csv
import json
import xmltodict
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

    def read_xml(path):
        with open(path) as file:
            content = xmltodict.parse(file.read())
            products = content["dataset"]["record"]
        return products

    def read_path_content(path):
        if path.endswith(".csv"):
            return Inventory.read_csv(path)
        if path.endswith(".json"):
            return Inventory.read_json(path)
        if path.endswith(".xml"):
            return Inventory.read_xml(path)

    def import_data(path, type):
        content = Inventory.read_path_content(path)

        if type == "simples":
            return SimpleReport.generate(content)

        if type == "completo":
            return CompleteReport.generate(content)
