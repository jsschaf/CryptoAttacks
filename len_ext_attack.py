import httplib, urlparse, sys
url = sys.argv[1]

# Your code to modify url goes here
tokenStart = url.index("=") + 1
tokenEnd = url.index("&")
token = url[tokenStart:tokenEnd]

print token 
#new command
newCommand = "&command3=UnlockAllSafes"

#create hash for new command ??
h = md5()
h.update(newCommand)
suffix = h.hexdigest()


parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
