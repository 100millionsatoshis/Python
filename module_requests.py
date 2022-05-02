# Python Requests Module makes a request to a webpage and prints the response text:
import requests
a = requests.get('https://w3schools.com/python/demopage.htm')
print(a.text)

# delete(url, args) Sends a DELETE request to the specified url
b = requests.delete('https://w3schools.com/python/demopage.php')
print(b.text)
# delete() method sends a DELETE request to the specified url.
# DELETE requests are made for deleting the specified resource (file, record etc).
# Syntax:
# requests.delete(url, args)

# args means zero or more of the named arguments in the parameter table below. Example:
# requests.delete(url, timeout=2.50)

# url: Required. The url of the request.

# allow_redirects: Optional. A Boolean to enable/disable redirection. Default True (allowing redirects)
# Sometimes the server redirects a request, could be if the file does not exist etc., set the 'allow_redirects'
# parameter False to deny redirects:
# x = requests.delete(url, allow_redirects=False)

# auth: Optional. A tuple to enable a certain HTTP authentication.
# Default None
# Use the 'auth' parameter to send requests with HTTP Basic Auth:
# x = requests.delete(url, auth = ('user', 'pass'))

# cert:
# Optional. A String or Tuple specifying a cert file or key.
# Default None
# Specify a cert to use as a client side certificate by setting the 'cert' parameter:
# x = requests.delete(url, cert='folder/my_client.cert')

# cookies:
# Optional. A dictionary of cookies to send to the specified url.
# Default None
# Use the 'cookies' parameter to send cookies to the server:
# x = requests.delete(url, cookies = {"fav_color": "Red"})

# headers:
# Optional. A dictionary of HTTP headers to send to the specified url.
# Default None
# use the 'headers' parameter to set the HTTP headers:
# x = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

# proxies
# Optional. A dictionary of the protocol to the proxy url.
# Default None
# find a free proxy address and send your request via that proxy:
# x = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(x.status_code)

# stream
# Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
# Default False
url = 'https://w3schools.com/images/pulpit.jpg'
# allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.delete(url, stream=True)
print(x.status_code)

# timeout
# Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or
# send a response.
# Default None which means the request will continue until the connection is closed
c = requests.delete('https://w3schools.com/python/demopage.php', timeout=5)
print(c.text)
url = 'https://w3schools.com/images/pulpit.jpg'

# verify
# Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
# Default True
# Make the request with the path to a TLS certificate:
# x = requests.delete(url, verify='folder/tlscertificate')
# Make the request and specify that there will be no verifying:
# x = requests.delete(url, verify=False)
