import json
import requests

def run_client():
    response = requests.get("http://127.0.0.1:5209/requestImage")
    print(response.text)

if __name__ == "__main__":
    run_client()