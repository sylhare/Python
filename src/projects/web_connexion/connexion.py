import json

import requests

TOKEN = ''
AUTH_HEADER = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(TOKEN)}
GITLAB_TOKEN_HEADER = {'Content-Type': 'application/json',
                       'PRIVATE-TOKEN': '{0}'.format(TOKEN)}


def print_ssh_keys_details(ssh_keys):
    """

    :param ssh_keys:
    :return:
    """
    if ssh_keys is not None:
        print("Here are your keys: ")
        for key, details in enumerate(ssh_keys['ssh_keys']):
            print("Key {}:".format(key))
            for k, v in details.items():
                print('  {0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')


def json_decode(response):
    if response is not None:
        return json.loads(response.content.decode('utf-8'))
    else:
        print('[!] Request Failed')
        return response


def get_token_gitlab_session(token, url):
    """

    :param token:
    :param url:
    :return:
    """

    header = {'Content-Type': 'application/json',
              'PRIVATE-TOKEN': '{0}'.format(token)}
    requests.packages.urllib3.disable_warnings()
    response = requests.Session().get(url, headers=header, verify=False)

    if response.status_code == 200:
        return json_decode(response)
    else:
        print("[?] Unexpected Error: [HTTP {0}]: Content: {1}".format(response.status_code, response.content))
    return None


def get_login_session(username, password, login_url):
    """

    :param login_url:
    :param username:
    :param password:
    """
    login_data = {'username': username, 'password': password}
    s = requests.Session()
    s.post(login_url, data=login_data)
    return s


def get_response(url, session=None):
    if session is None:
        session = requests.session()

    response = session.get(url)

    if response.status_code == 200:
        return response
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, url))
        return None


def error_handling_post(response):
    """
    Check if the status code and return response if all clear
    :param response:
    :return:
    """
    if response.status_code > 499:
        print("[!] [{0}] Server Error".format(response.status_code))
        return None
    elif response.status_code == 404:
        print("[!] [{0}] URL not found: [{1}]".format(response.status_code, response.url))
        return None
    elif response.status_code == 401:
        print("[!] [{0}] Authentication Failed".format(response.status_code))
        return None
    elif response.status_code > 399:
        print("[!] [{0}] Bad Request".format(response.status_code))
        print(response.content)
        return None
    elif response.status_code > 299:
        print("[!] [{0}] Unexpected redirect.".format(response.status_code))
        return None
    elif response.status_code == 201:
        return response
    else:
        print("[?] Unexpected Error: [HTTP {0}]: Content: {1}".format(response.status_code, response.content))
        return None


def error_handling_get(response):
    """
    Check if the status code and return response if all clear
    :param response:
    :return:
    """
    if response.status_code >= 500:
        print("[!] [{0}] Server Error".format(response.status_code))
        return None
    elif response.status_code == 404:
        print("[!] [{0}] URL not found: [{1}]".format(response.status_code, response.url))
        return None
    elif response.status_code == 401:
        print("[!] [{0}] Authentication Failed".format(response.status_code))
        return None
    elif response.status_code == 400:
        print("[!] [{0}] Bad Request".format(response.status_code))
        return None
    elif response.status_code >= 300:
        print("[!] [{0}] Unexpected Redirect".format(response.status_code))
        return None
    elif response.status_code == 200:
        return response
    else:
        print("[?] Unexpected Error: [HTTP {0}]: Content: {1}".format(response.status_code, response.content))
    return None


if __name__ == '__main__':
    url = ""
    token = ""
    headers = AUTH_HEADER
    requests.packages.urllib3.disable_warnings()
    with requests.Session() as s:
        r = s.get(url, headers=headers, verify=False)
        json_data = json.loads(r.text)
        arr = r.json()
