from typing import Dict, Union

from splunk_api import send_json
import csv
import click
import datetime

DATE_FORMAT = "%d/%m/%Y"


@click.command
@click.option(
    "-f",
    "--csv_file_path",
    help="The path to the csv file downloaded from isracard site.",
)
@click.option("-t", "--token", help="The HEC (HTTP Event Collector) from your splunk instance")
def upload_csv_to_splunk(csv_file_path: str, token: str):
    with open(csv_file_path, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)

        for row in csv_reader:
            data = _parse_row(row)
            if data:
                send_json(data["data"], data["timestamp"], token)


def _parse_row(row: Dict[str, str]) -> dict[str, Union[str, dict, float]]:
    if len(row.get("תאריך רכישה", "").replace(" ", "")) > 1:
        return {
            "data": {
                "Price": row["סכום חיוב"],
                "Business": row["שם בית עסק"].replace('"', "").replace("'", "").replace(" ", "_"),
                "Date": row["תאריך רכישה"],
            },
            "timestamp": datetime.datetime.strptime(row["תאריך רכישה"], DATE_FORMAT).timestamp(),
        }

    else:
        return {}


if __name__ == "__main__":
    upload_csv_to_splunk()
