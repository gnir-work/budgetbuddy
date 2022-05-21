import csv
import json
import requests

SPLUNK_URL = "https://localhost:8088/services/collector/event"

AUTH_HEADER = "Splunk 3e278124-e71f-465a-9467-9df69289010a"

HEADERS = {"Authorization": AUTH_HEADER}


def send(data: dict):
    print(
        requests.post(
            SPLUNK_URL, headers=HEADERS, json=dict(event=data), verify=False
        ).text
    )


def make_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            if len(rows["\ufeffתאריך רכישה"].replace(" ", "")) > 1:

                eng = {
                    "Price": rows["סכום חיוב"],
                    "Business": rows["שם בית עסק"]
                    .replace('"', "")
                    .replace("'", "")
                    .replace(" ", "_"),
                    "Date": rows["\ufeffתאריך רכישה"],
                }

                send(eng)

    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


csvFilePath = r"utfbank.csv"
jsonFilePath = r"bank.json"

make_json(csvFilePath, jsonFilePath)
