#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    try:
        data = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": q}).json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
