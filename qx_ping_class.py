import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

class Qx_ping:
    def __init__(self, dst_ip):
        self.dst_ip = dst_ip
        self.length = 20
        self.srcip = '192.168.56.1'
        self.ping_pkt = IP(dst=self.dst_ip, len=self.length) / ICMP() / 'abc'
        self.ping_result = sr1(self.ping_pkt, timeout=2, verbose=False)

    def one(self):
        self.ping_result.show()

    def ping(self):
        for x in range(5):
            if self.ping_result:
                print('!', end='')
            else:
                print('.', end='')


if __name__ == '__main__':
    ping = Qx_ping('172.17.1.3')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s*int((70-len(word))/2), word, s*int((70-len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('print one for sure reachable')
    ping.one()
    print_new('ping five ')
    ping.ping()