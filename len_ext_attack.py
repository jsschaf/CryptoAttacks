import httplib, urlparse, sys
from pymd5 import md5, padding

url = sys.argv[1]


# Your code to modify url goes here
tokenStart = url.index("=") + 1
tokenEnd = url.index("&")
token = url[tokenStart:tokenEnd]
print token


#new command
newCommand = "&command3=UnlockAllSafes"


#create hash for new command ??
tokenLength = 8 + len(url[(tokenEnd + 1):]) #password + length of end part of URL
numBits = 8*tokenLength
h = md5(state = token.decode("hex"), count = numBits)
h.update(newCommand)
suffix = h.hexdigest()



parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
