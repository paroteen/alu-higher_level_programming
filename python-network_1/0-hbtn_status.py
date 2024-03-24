import urllib.request

url = "https://alu-intranet.hbtn.io/status"

# Fetch the URL and read the response
with urllib.request.urlopen(url) as response:
    # Read the content of the response
    content = response.read()
    
    # Convert the content to utf-8 format
    utf8_content = content.decode('utf-8')

# Display the body of the response
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", utf8_content)
