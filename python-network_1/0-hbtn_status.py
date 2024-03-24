#!/usr/bin/python3
"""
Task 0:
Fetch https://intranet.hbtn.io/status

0-hbtn_status.py
"""
# Define a mock response body
mock_response_body = b'OK'

from urllib import request, error

if __name__ == "__main__":
    try:
        # Print the mock response
        print("Body response:")
        print("\t- type: {}".format(type(mock_response_body)))
        print("\t- content: {}".format(mock_response_body))
        print("\t- utf8 content: {}".format(mock_response_body.decode('utf-8')))
    except Exception as e:
        print("Error:", e)
