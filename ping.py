import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip
    else:
        return 0


if __name__ == "__main__":
    if ping('172.17.1.3'):
        print('!')
    else:
        print('.')




