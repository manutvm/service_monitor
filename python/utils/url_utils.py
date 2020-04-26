import requests


def get_url_contents(url):
    response_code = None
    response_message = None
    try:
        json_response = requests.get(url)
        response_code = json_response.status_code
        response_message = json_response.text
    except requests.exceptions.ConnectionError as ex:
        response_code = 500
        response_message = None

    return response_code, response_message