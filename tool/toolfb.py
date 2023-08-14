import ppadb
from ppadb.client import Client as AdbClient
import os

thread = 4
print(os.getcwd())
# class Devices:
#     def __int__(str, x, y):
#         str.x = x
#         str.y = y
#     def showLocationIcon(self):
#         print(self.x, self.y)
#         print(self)
#
# # def get
# def getDevice():
#     # Default is "127.0.0.1" and 5037
#     try:
#         client = AdbClient(host="127.0.0.1", port=5037)
#         devices = client.devices()
#         for device in devices:
#             device.input_tap(891, 259)
#         # return devices[i]
#     except Exception as e:
#         return False
# getDevice()

fd = 'test.txt'

file = open(fd, 'r')
text = file.read()
print(text)

