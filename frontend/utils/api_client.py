import os
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def get(path: str, params: dict = None):
    try:
        response = requests.get(
            f"{BACKEND_URL}{path}",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def post(path: str, json_body: dict = None):
    try:
        response = requests.post(
            f"{BACKEND_URL}{path}",
            json=json_body,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def put(path: str, json_body: dict = None):
    try:
        response = requests.put(
            f"{BACKEND_URL}{path}",
            json=json_body,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def delete(path: str):
    try:
        response = requests.delete(
            f"{BACKEND_URL}{path}",
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None