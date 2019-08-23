import sys, socket

internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
internal_ip.connect(('google.com', 0))
print(internal_ip.getsockname())