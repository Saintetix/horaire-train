
from flask import Flask, request, render_template
import requests, json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    call_api_sncf()

    stop_areas = json.loads((find_places(request.args.get('from_stop_area', ''))).text)["places"]
    for stop_area in stop_areas:
        print(stop_area["name"])

    routes = get_routes()

    return (
            render_template("index.html", stop_areas=stop_areas)
            + str(routes.json())
        )

def call_api_sncf(seed=''):
    url = f'https://api.sncf.com/v1/{seed}'
    token = 'aca917c8-7a2b-4053-ad13-391398c7c4ba'
    response = requests.get(url, auth=(token, ''))

    print(f'URL = {url}')
    print(f'CONNECT API = {response}')

    return response

def find_places(stop_area=''):
    response = call_api_sncf(f'coverage/sncf/places?q={stop_area}')

    print(f'GET PLACES = {response}')

    return response

def get_routes():
    now = datetime.now().strftime("%Y%m%dT%H%M%S")
    from_stop_area = ''
    to_stop_area = ''

    response = call_api_sncf(f'coverage/sncf/journeys?from={from_stop_area}&to={to_stop_area}&datetime={now}')

    print(f'GET ROUTES = {response}')

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)