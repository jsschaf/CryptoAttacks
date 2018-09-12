from pymd5 import md5, padding

m = "Use HMAC, not hashes" 

print md5(m).hexdigest()

bits = (21 + len(padding(21 * 8))) * 8

print bits

h = md5(state="3ecc68efa1871751ea9b0b1a5b25004d".decode("hex"), count=512)

x = "Good advice"
h.update(x)

print h.hexdigest()