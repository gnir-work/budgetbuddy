from typing import Dict

from splunk_api import send_json
import csv
import click


@click.command
@click.option(
    "-f",
    "--csv_file_path",
    help="The path to the csv file downloaded from isracard site.",
)
@click.option(
    "-t", "--token", help="The HEC (HTTP Event Collector) from your splunk instance"
)
def upload_csv_to_splunk(csv_file_path: str, token: str):
    with open(csv_file_path, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)

        for row in csv_reader:
            data = _parse_row(row)
            if data:
                send_json(data, token)


def _parse_row(row: Dict[str, str]) -> Dict[str, str]:
    if len(row.get("תאריך רכישה", "").replace(" ", "")) > 1:
        return {
            "Price": row["סכום חיוב"],
            "Business": row["שם בית עסק"]
            .replace('"', "")
            .replace("'", "")
            .replace(" ", "_"),
            "Date": row["תאריך רכישה"],
        }

    else:
        return {}


if __name__ == "__main__":
    upload_csv_to_splunk()
