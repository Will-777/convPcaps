"""

Simple Pairwise Master Key generator

"""

from pbkdf2 import PBKDF2
import binascii

ssid = 'home'
phrase = 'qwerty123'
print("SSID: {}".format(ssid))
print("Pass phrase: {}".format(phrase))
PMKey_Bytes = PBKDF2(phrase, ssid, 4096).read(32)
PMKey = binascii.hexlify(PMKey_Bytes)
print("Pairwise Master Key: " + PMKey)

