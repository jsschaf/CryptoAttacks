from roots import *
import hashlib, sys
message = sys.argv[1]

#-----BEGIN PUBLIC KEY-----
key = """MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA6zf/W1NAwrs6gRr94ULW
8DcApVRkuZHInGVL6HhUFRTsbuTWWWLHWFJQATfAeySb3uPvbmAEAp9Lfrow5zLL
c4So2xse8EDvb8lWdTC4WP4LtYmWqiGHc6qJnKUMHx8mxHrElvHAOVVAJzvmCuGv
Sb2rxFLEEFxgw0CNUJ6CCSqN6Vc3176sqVC3a7vqyB+VojcVIQYVRpMjsxks+daU
N0PCdF22kVL6mDg+MmsMnLqS10F1sU+W+BCivRU+0dZgrX89jKam7V4g8neVYsi4
qJsXjJizIHsHF2WUPLNETTMU2+sNfpuVMeUaKR34wE6vP2XeFWpRH8piUKtcqsqZ
dQIBAw=="""
#-----END PUBLIC KEY-----

e = 3
k = 2048

arbitrary = '00'
digest = hashlib.sha256(message).hexdigest()

signature = '0x0001FF003031300d060960864801650304020105000420'

print signature
forged_signature = signature + digest

for i in range(k/8 - 55):
	forged_signature = forged_signature + arbitrary

print forged_signature

[forged_signature, worked] = integer_nthroot(bytes_to_integer(forged_signature), 3)

print forged_signature
print hex(forged_signature)

#print integer_to_bytes(forged_signature)

#forged_signature = integer_nthroot(forged_signature, 3)

print integer_to_base64(forged_signature)