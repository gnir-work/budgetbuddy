import requests
from typing import Dict

SPLUNK_URL = "https://localhost:8088/services/collector/event"
AUTH_HEADER_FORMAT = "Splunk {token}"


def _generate_headers(token: str) -> Dict[str, str]:
    return {"Authorization": AUTH_HEADER_FORMAT.format(token=token)}


def send_json(data: dict, timestamp: int, token: str):
    response = requests.post(
        SPLUNK_URL,
        headers=_generate_headers(token),
        json=dict(event=data, time=timestamp),
        verify=False,
    )
    response.raise_for_status()
