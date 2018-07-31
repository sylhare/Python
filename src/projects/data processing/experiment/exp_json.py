"""
http://docs.python-guide.org/en/latest/scenarios/json/
https://code.tutsplus.com/tutorials/how-to-work-with-json-data-using-python--cms-25758
https://pythontips.com/2013/08/08/storing-and-loading-data-with-json/

"""

import json


def jsonDefault(object):
    """
    Return a dictionary out of the object
    """
    return object.__dict__


class Person(object):
    """
    Model for a person
    """
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


if __name__ == "__main__":
    # From python dictionary to json
    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
    }
    print(json.dumps(d))

    # From json to python dictionary
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
    parsed_json = json.loads(json_string)
    # print(parsed_json['first_name'])
    print(parsed_json)

    # Using a class to json
    guido = Person("Guido", "Rossum")
    jsonGuido = json.dumps(guido, default=jsonDefault)
    print(jsonGuido)
