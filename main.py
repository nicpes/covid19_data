from flask import Flask
from flask_cors import CORS, cross_origin
from ast import dump
from audioop import reverse
import re, json, requests
import pandas as pd

regions_total_cases = [
    {"nome": "Abruzzo", "totale": 0, "data": ""},
    {"nome": "Basilicata", "totale": 0, "data": ""},
    {"nome": "Calabria", "totale": 0, "data": ""},
    {"nome": "Campania", "totale": 0, "data": ""},
    {"nome": "Emilia-Romagna", "totale": 0, "data": ""},
    {"nome": "Friuli Venezia Giulia", "totale": 0, "data": ""},
    {"nome": "Lazio", "totale": 0, "data": ""},
    {"nome": "Liguria", "totale": 0, "data": ""},
    {"nome": "Lombardia", "totale": 0, "data": ""},
    {"nome": "Marche", "totale": 0, "data": ""},
    {"nome": "Molise", "totale": 0, "data": ""},
    {"nome": "P.A. Bolzano", "totale": 0, "data": ""},
    {"nome": "P.A. Trento", "totale": 0, "data": ""},
    {"nome": "Piemonte", "totale": 0, "data": ""},
    {"nome": "Puglia", "totale": 0, "data": ""},
    {"nome": "Sardegna", "totale": 0, "data": ""},
    {"nome": "Sicilia", "totale": 0, "data": ""},
    {"nome": "Toscana", "totale": 0, "data": ""},
    {"nome": "Umbria", "totale": 0, "data": ""},
    {"nome": "Valle d'Aosta", "totale": 0, "data": ""},
]


def main():

    inputValue = input(
        "For today data enter 'today' or press Enter to select another date:  "
    )
    # IF inputValue RECEIVES "today" AS VALUE, THE JSON FILE RELATIVE TO 2022 IS FETCHED AND FILTERED, IF THE USER JUST PRESS ENTER, THEN HE CAN ENTER A DATE TO FILTER ANOTHER JSON FILE WITH DATA OF 2020 + #

    if inputValue == "today":
        url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json"
        resp = requests.get(url)
        resp_parsed = re.sub(r"^jsonp\d+\(|\)\s+$", "", resp.text)
        data = json.loads(resp_parsed)

        for i in data:
            for r in regions_total_cases:
                if i["denominazione_regione"] == r["nome"]:
                    r["totale"] += i["totale_casi"]
                    r["data"] = i["data"]

        regions_total_cases.sort(key=lambda s: s["nome"], reverse=True)

        regions_total_cases.sort(key=lambda s: s["totale"], reverse=True)

        print(regions_total_cases)

        # WRITING DATA ON EXCEL FILE #

        excel_data = pd.DataFrame(regions_total_cases)

        excel = pd.ExcelWriter(
            "./xls_reports/covid_19_today_data.xlsx", engine="xlsxwriter"
        )

        excel_data.to_excel(excel, sheet_name="Sheet1")

        excel.save()

    else:

        date = input("insert data yyyy-mm-dd: ")

        url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json"
        resp = requests.get(url)
        resp_parsed = re.sub(r"^jsonp\d+\(|\)\s+$", "", resp.text)
        data = json.loads(resp_parsed)

        for i in data:
            if date in i["data"]:
                for r in regions_total_cases:
                    if i["denominazione_regione"] == r["nome"]:
                        r["totale"] += i["totale_casi"]
                        r["data"] = i["data"]

        regions_total_cases.sort(key=lambda s: s["nome"])

        regions_total_cases.sort(key=lambda s: s["totale"], reverse=True)

        print(regions_total_cases)

        excel_data = pd.DataFrame(regions_total_cases)

        excel = pd.ExcelWriter("./xls_reports/covid_19_data.xlsx", engine="xlsxwriter")

        excel_data.to_excel(excel, sheet_name=f"covid_19_data")

        excel.save()




if __name__ == '__main__':
    main()

