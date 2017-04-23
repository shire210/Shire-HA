import argparse
import json
import requests

def main():

    token = _get_token("mrossiter21@gmail.com", "1522Huntly")
    if token is not None:
    	_get_user(token)


def _get_token(username, password):
        payload = {'username': username, 'password': password}
        token_response = requests.post("https://winkbearertoken.appspot.com/token", data=payload)
        try:
            return token_response.text.split(':')[1].split()[0].rstrip('<br')
        except IndexError:
            return None


def _get_user(token):
        api_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token),
            "User-Agent": "Manufacturer/python-wink python/3 Wink/3"
        }
        url_string = "https://api.wink.com/users/me/wink_devices/"
        arequest = requests.get(url_string, headers=api_headers)
        print(json.dumps(arequest.json(), sort_keys=True, indent=4))


if __name__ == "__main__":
    main()
