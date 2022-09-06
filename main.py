from ast import dump
from audioop import reverse
import re, json, requests
import pandas as pd




inputValue = input("For today data enter 'today' or press Enter to select another date:  ")

# IF inputValue RECEIVES "today" AS VALUE THE JSON FILE RELATIVE TO 2022 IS FETCHED AND FILTERED, IF THE USER JUST PRESS ENTER, THEN HE CAN ENTER A DATE TO FILTER ANOTHER JSON FILE WITH DATA OF 2020 + 

if inputValue == "today":
    url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json'
    resp = requests.get(url)
    resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', resp.text)
    data = json.loads(resp_parsed)


    regions_total_cases = [{"nome" : "Abruzzo", "totale" : 0}, {"nome" : "Basilicata", "totale" : 0}, {"nome" : "Calabria", "totale" : 0}, {"nome" : "Campania", "totale" : 0}, {"nome" : "Emilia-Romagna", "totale" : 0}, {"nome" : "Friuli Venezia Giulia", "totale" : 0}, {"nome" : "Lazio", "totale" : 0}, {"nome" : "Liguria", "totale" : 0}, {"nome" : "Lombardia", "totale" : 0}, {"nome" : "Marche" , "totale" :  0}, {"nome" : "Molise", "totale" : 0}, {"nome" : "P.A. Bolzano", "totale" : 0}, {"nome" : "P.A. Trento", "totale" :  0}, {"nome" : "Piemonte", "totale" : 0}, {"nome" : "Puglia", "totale" :  0}, {"nome" : "Sardegna", "totale" :  0}, {"nome" : "Sicilia", "totale" : 0}, {"nome" : "Toscana", "totale" : 0}, {"nome" : "Umbria", "totale" : 0}, {"nome" : "Valle d'Aosta", "totale" : 0} ]

    for i in data:
        for r in regions_total_cases:
            if i["denominazione_regione"] == r["nome"]:
                r["totale"] += i["totale_casi"]


    regions_total_cases.sort(key=lambda s: s["nome"], reverse=True)

    regions_total_cases.sort(key=lambda s: s["totale"], reverse=True)

    print(regions_total_cases)

    excel_data  = pd.DataFrame(regions_total_cases)

    excel = pd.ExcelWriter("covid_19_today_data.xlsx", engine="xlsxwriter")

    excel_data.to_excel(excel, sheet_name="Sheet1")

    excel.save()


else:
    date = input("insert data yy-mm-dd: ")

    url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json'
    resp = requests.get(url)
    resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', resp.text)
    data = json.loads(resp_parsed)

    regions_total_cases = [{"nome" : "Abruzzo", "totale" : 0}, {"nome" : "Basilicata", "totale" : 0}, {"nome" : "Calabria", "totale" : 0}, {"nome" : "Campania", "totale" : 0}, {"nome" : "Emilia-Romagna", "totale" : 0}, {"nome" : "Friuli Venezia Giulia", "totale" : 0}, {"nome" : "Lazio", "totale" : 0}, {"nome" : "Liguria", "totale" : 0}, {"nome" : "Lombardia", "totale" : 0}, {"nome" : "Marche" , "totale" :  0}, {"nome" : "Molise", "totale" : 0}, {"nome" : "P.A. Bolzano", "totale" : 0}, {"nome" : "P.A. Trento", "totale" :  0}, {"nome" : "Piemonte", "totale" : 0}, {"nome" : "Puglia", "totale" :  0}, {"nome" : "Sardegna", "totale" :  0}, {"nome" : "Sicilia", "totale" : 0}, {"nome" : "Toscana", "totale" : 0}, {"nome" : "Umbria", "totale" : 0}, {"nome" : "Valle d'Aosta", "totale" : 0} ]

    for i in data:
        if date in i["data"]:
            for r in regions_total_cases:
                    if i["denominazione_regione"] == r["nome"]:
                        r["totale"] += i["totale_casi"]


    regions_total_cases.sort(key=lambda s: s["nome"])

    regions_total_cases.sort(key=lambda s: s["totale"], reverse=True)

    print(regions_total_cases)

    excel_data  = pd.DataFrame(regions_total_cases)

    excel = pd.ExcelWriter("covid_19_data.xlsx", engine="xlsxwriter")

    excel_data.to_excel(excel, sheet_name=f"covid_19_data")

    excel.save()
