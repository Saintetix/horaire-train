from flask import Flask
from flask import request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    response = connect_api_sncf()
    routes = get_routes()

    return (
            """Horaire train :"""
            + str(routes.json())
        )

def connect_api_sncf():
    try:
        url = 'https://api.sncf.com/v1'
        token = 'aca917c8-7a2b-4053-ad13-391398c7c4ba'
        response = requests.get(url, auth=(token, ''))

        print('CONNECT API = ' + str(response))

        return response
    except ValueError:
        return "Can't connect to api"

def get_routes():
    try:
        now = datetime.now().strftime("%Y%m%dT%H%M%S")
        url = 'https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area%3ASNCF%3A87723197&to=stop_area%3ASNCF%3A87726000'
        token = 'aca917c8-7a2b-4053-ad13-391398c7c4ba'
        response = requests.get(url, auth=(token, ''))

        print('GET ROUTES = ' + str(response))

        return response
    except ValueError:
        return "Can't connect to api"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)