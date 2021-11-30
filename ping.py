import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    print(ping_result)
    if ping_result:
        return ip
    else:
        return 0





