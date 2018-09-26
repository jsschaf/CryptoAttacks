from roots import *
import hashlib
import sys
message = sys.argv[1]

#begin public key
#message = """
#    MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA6zf/W1NAwrs6gRr94ULW
#8DcApVRkuZHInGVL6HhUFRTsbuTWWWLHWFJQATfAeySb3uPvbmAEAp9Lfrow5zLL
#c4So2xse8EDvb8lWdTC4WP4LtYmWqiGHc6qJnKUMHx8mxHrElvHAOVVAJzvmCuGv
#Sb2rxFLEEFxgw0CNUJ6CCSqN6Vc3176sqVC3a7vqyB+VojcVIQYVRpMjsxks+daU
#N0PCdF22kVL6mDg+MmsMnLqS10F1sU+W+BCivRU+0dZgrX89jKam7V4g8neVYsi4
#qJsXjJizIHsHF2WUPLNETTMU2+sNfpuVMeUaKR34wE6vP2XeFWpRH8piUKtcqsqZ
#dQIBAw==
#"""
#end public key

#The signature must use the SHA-256 digest of a string with the following form
#from_account+to_account+amount

#signature has:
#bytes: 00 01
#random number of FF so that total length = key size
# sha-256 digest
#201*00 arbitrary bytes

sha = hashlib.sha256(message).hexdigest()

signature = "0x0001FF003031300d060960864801650304020105000420" + str(sha)

string = "00"

for i in range(200):
    string += "00"

signature += string;

sig = int(signature,16)

[forged_signature, worked] = integer_nthroot(sig, 3)

if (worked == 0):
    forged_signature += 1; #to account for the rounding of integers

print integer_to_base64(forged_signature)

