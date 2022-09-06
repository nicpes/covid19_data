from ast import dump
from audioop import reverse
import re, json, requests

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
print(dt_string)



url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json'

resp = requests.get(url)
resp_parsed = re.sub(r'^jsonp\d+\(|\)\s+$', '', resp.text)
data = json.loads(resp_parsed)


regions_total_cases = [{"nome" : " Abruzzo", "totale" : 0}, {"nome" : "Basilicata", "totale" : 0}, {"nome" : "Calabria", "totale" : 0}, {"nome" : "Campania", "totale" : 0}, {"nome" : "Emilia-Romagna", "totale" : 0}, {"nome" : "Friuli_Venezia_Giulia", "totale" : 0}, {"nome" : "Lazio", "totale" : 0}, {"nome" : "Liguria", "totale" : 0}, {"nome" : "Lombardia", "totale" : 0}, {"nome" : "Marche" , "totale" :  0}, {"nome" : "Molise", "totale" : 0}, {"nome" : "P.A. Bolzano", "totale" : 0}, {"nome" : "P.A. Trento", "totale" :  0}, {"nome" : "Piemonte", "totale" : 0}, {"nome" : "Puglia", "totale" :  0}, {"nome" : "Sardegna", "totale" :  0}, {"nome" : "Sicilia", "totale" : 0}, {"nome" : "Toscana", "totale" : 0}, {"nome" : "Umbria", "totale" : 0}, {"nome" : "Valle d'Aosta", "totale" : 0} ]

for i in data:
    if "2022" in i["data"]:
        for r in regions_total_cases:
                if i["denominazione_regione"] == r["nome"]:
                    r["totale"] += i["totale_casi"]


regions_total_cases.sort(key=lambda s: s["nome"], reverse=True)

regions_total_cases.sort(key=lambda s: s["totale"], reverse=True)

print(regions_total_cases)
