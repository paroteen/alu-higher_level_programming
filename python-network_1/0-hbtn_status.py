#!/usr/bin/python3
from urllib import request, error

if __name__ == "__main__":
    try:
        req = request.Request('https://intranet.hbtn.io/status')
        with request.urlopen(req) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except error.HTTPError as e:
        if e.code == 403:  # Forbidden error code
            print("Failed to fetch URL: Forbidden - You may not have permission to access the resource.")
        else:
            print("Failed to fetch URL:", e.code, e.reason)
    except error.URLError as e:
        print("Failed to fetch URL:", e.reason)
    except Exception as e:
        print("Error:", e)
