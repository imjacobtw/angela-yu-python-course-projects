from datetime import datetime
from dotenv import dotenv_values
import requests

config = dotenv_values(".env")

PIXELA_API_BASE_URL = "https://pixe.la/v1/users"
PIXELA_API_TOKEN = config["PIXELA_API_TOKEN"]
PIXELA_API_USERNAME = config["PIXELA_API_USERNAME"]


def create_user() -> None:
    url = PIXELA_API_BASE_URL
    params = {
        "token": PIXELA_API_TOKEN,
        "username": PIXELA_API_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=url, json=params)
    print(response.text)


def create_graph(id: str, name: str, unit: str, type: str, color: str) -> None:
    url = f"{PIXELA_API_BASE_URL}/{PIXELA_API_USERNAME}/graphs"
    params = {
        "id": id,
        "name": name,
        "Unit": unit,
        "type": type,
        "color": color,
    }
    headers = {"X-USER-TOKEN": PIXELA_API_TOKEN}
    response = requests.post(url=url, json=params, headers=headers)
    print(response.text)


def create_pixel(graph_id: str, date: datetime, quantity: int) -> None:
    url = f"{PIXELA_API_BASE_URL}/{PIXELA_API_USERNAME}/graphs/{graph_id}"
    params = {
        "date": date.strftime("%Y%m%d"),
        "quantity": str(quantity),
    }
    headers = {"X-USER-TOKEN": PIXELA_API_TOKEN}
    response = requests.post(url=url, json=params, headers=headers)
    print(response.text)


def update_pixel(graph_id: str, date: datetime, quantity: int) -> None:
    url = f"{PIXELA_API_BASE_URL}/{PIXELA_API_USERNAME}/graphs/{graph_id}/{date.strftime("%Y%m%d")}"
    params = {"quantity": str(quantity)}
    headers = {"X-USER-TOKEN": PIXELA_API_TOKEN}
    response = requests.put(url=url, json=params, headers=headers)
    print(response.text)


def delete_pixel(graph_id: str, date: datetime) -> None:
    url = f"{PIXELA_API_BASE_URL}/{PIXELA_API_USERNAME}/graphs/{graph_id}/{date.strftime("%Y%m%d")}"
    headers = {"X-USER-TOKEN": PIXELA_API_TOKEN}
    response = requests.delete(url=url, headers=headers)
    print(response.text)


# create_graph("graph1", "Reading Graph", "Pages", "int", "sora")
# create_pixel("graph1", datetime.now(), 5)
# update_pixel("graph1", datetime.now(), 10)
# delete_pixel("graph1", datetime.now())
