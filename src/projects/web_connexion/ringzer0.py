#!/usr/bin/python3
# https://github.com/F00ker/ringzer0
import hashlib
import re

import requests

url = 'https://ringzer0team.com/challenges/56'
login_url = 'https://ringzer0team.com/login'
text_regex = '----- BEGIN MESSAGE -----<br />\r\n\t\t(\w+)'
text_regex_2 = '----- BEGIN HASH -----<br />\r\n\t\t(\w+)'
flag_regex = 'FLAG-\w+'
wrong_regex = 'Wrong.*!'
session = requests.session()


def hash_sha512(text):
    """

    :param text:
    :return:
    """
    return hashlib.sha512(text).hexdigest()


def hash_sha1(text):
    """

    :param text:
    :return:
    """
    return hashlib.sha1(text).hexdigest()


def crack_ringzero56_sha1(sha1_msg):
    answer = ''

    for i in range(1000, 10000):
        if hash_sha1(str(i)) == sha1_msg:
            answer = str(i)
            print(answer)

    return answer


def bit_in_bytes_to_string(binary_str):
    result = ''

    for i in range(0, len(binary_str), 8):
        eight_bits_to_int = int(binary_str[i:i + 8], 2)
        int_to_char = chr(eight_bits_to_int)
        result += int_to_char

    return result


def get_flag(text):
    """

    :param username: 
    :param password: 
    :return: 
    """

    flag = re.search(flag_regex, text)
    wrong = re.search(wrong_regex, text)
    if flag:
        print(flag.group())
        return flag.group()
    elif wrong:
        return wrong.group()
    else:
        return 'Unknown Error!'


def get_text(text):
    """

    :param username:
    :param password:
    :return:
    """
    text = re.search(text_regex, text)
    return text.group(1)


def con_old(username, password, url):
    """

    :param username: 
    :param password: 
    :param url: 
    """
    login_data = {'username': username, 'password': password}
    s = requests.Session()
    s.post(login_url, auth=(username, password), data=login_data)
    COOKIES = dict(PHPSESSID='**********************')
    cookies = requests.utils.dict_from_cookiejar(s.cookies)
    # page = s.get(url, cookies=cookies)
    page = s.get(url)
    print(page.content)
    print(requests.utils.dict_from_cookiejar(s.cookies))


def connexion_using_with(username, password, url):
    """

    :param username:
    :param password:
    :param url:
    """
    login_data = {'username': username, 'password': password}
    with requests.Session() as s:
        s.post(login_url, data=login_data)
        r = s.get(url)

        text = re.search(text_regex, r.text)
        answer = s.post(url + '/' + str(hash_sha512(text.group(1))))
        flag = re.search(flag_regex, answer.text)

        print(r.content)
        print(requests.utils.dict_from_cookiejar(s.cookies))
        print(flag.group())


def connexion_login(username, password, login_url):
    """

    :param username:
    :param password:
    :param url:
    """
    login_data = {'username': username, 'password': password}
    s = requests.Session()
    s.post(login_url, data=login_data)
    return s


def use_logged_in_connexion_13(s, url):
    r = s.get(url)

    text = re.search(text_regex, r.text)
    answer = s.post(url + '/' + str(hash_sha512(text.group(1))))
    flag = re.search(flag_regex, answer.text)

    print(text.group(1))
    print(requests.utils.dict_from_cookiejar(s.cookies))
    print(flag)


def use_logged_in_connexion_14(s, url):
    r = s.get(url)

    text = re.search(text_regex, r.text)

    text_converted = bit_in_bytes_to_string(text.group(1))
    answer = s.post(url + '/' + str(hash_sha512(text_converted)))

    get_flag(answer.text)


def use_logged_in_connexion_56(s, url):
    r = s.get(url)

    text = re.search(text_regex_2, r.text)
    text_converted = crack_ringzero56_sha1(text.group(1))
    answer = s.post(url + '/' + text_converted)

    print(text_converted)
    get_flag(answer.text)


def use_logged_in_connexion(s, url):
    r = s.get(url)

    text = re.search(text_regex_2, r.text)
    text_converted = crack_ringzero56_sha1(text.group(1))
    answer = s.post(url + '/' + text_converted)

    print(text_converted)
    get_flag(answer.text)


if __name__ == '__main__':
    session = connexion_login('user', 'password', login_url)
    use_logged_in_connexion(session, url)
    crack_ringzero56_sha1("f4669fc3bb951a59f8987c1d4441605a11666a90")
    # Carve a message for hashing
    # message = re.findall(re.compile('----- BEGIN MESSAGE -----<br />[\r\n\s]*(.+?)[\r\n\s]*<br />'), page_task.text)
    # print message[0]
    # Get a hash_sha512 from message
    # message_hash = hashlib.sha512(message[0])
    # print message_hash.hexdigest()

    # Send our hash_sha512 to server
    # page_answer = my_session.get('http://ringzer0team.com/challenges/13/' + message_hash.hexdigest())
    # print page_answer.content

    # Get final flag from response page
    # my_flag = 'FLAG-' + re.findall('<div class="alert alert-info">FLAG-(.+?)</div>', page_answer.text)[0]
    # print my_flag
