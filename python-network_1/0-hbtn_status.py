#!/usr/bin/python3
"""
Task 0:
Fetch https://intranet.hbtn.io/status

0-hbtn_status.py
"""

import urllib

if __name__ == "__main__":
    try:
        req = urllib.request.Request('https://intranet.hbtn.io/status')
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Failed to fetch URL:", e.reason)
    except Exception as e:
        print("Error:", e)
