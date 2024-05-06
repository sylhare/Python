#!/bin/python3

import math

import requests


#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#

def avgRotorSpeed(status_query, parent_id):
    response = get_devices_json(status_query, 0)
    total_pages = int(response["total_pages"])
    data = response["data"]

    for page in range(1, total_pages):
        data = data + get_devices_json(status_query, page)["data"]
        print(data)

    matching_devices = filter(lambda device: is_parent(device, parent_id), data)

    return get_average_rotor_speed_from(matching_devices)


def get_average_rotor_speed_from(matching_devices):
    average_rotor_speed_list = list(map(lambda device: int(device["operatingParams"]["rotorSpeed"]), matching_devices))
    if len(average_rotor_speed_list) == 0:
        average_rotor_speed = 0
    else:
        average_rotor_speed = math.floor(sum(average_rotor_speed_list) / len(average_rotor_speed_list))
    return average_rotor_speed


def is_parent(device, parent_id):
    # return 'parent' in device.keys() and device['parent'] is not None and device['parent']['id'] == parentId
    try:
        return device["parent"]["id"] == parent_id
    except KeyError:
        return False  # no parent key
    except TypeError:
        return False  # parent = None


def get_devices_json(status_query, page_number):
    return requests.get("https://jsonmock.hackerrank.com/api/iot_devices/search?status={}&page={}"
                        .format(status_query, page_number)).json()


if __name__ == '__main__':
    pass
