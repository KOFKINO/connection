from ping import ping
from router_ssh import qx_multi_cmd
import re
import pprint


def get_int(*ips, username='admin', password='H3c.com!123'):
    device_if_dict = {}
    for ip in ips:
        one_dict = {}
        if ping(ip):
            result = qx_multi_cmd(ip, username, password, 'dis ip int brief')
            for res2 in result.split('\n'):
                int_infor = re.findall(r'(\S+)\s+\S+\s+\S+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', res2)
                if int_infor:
                    one_dict[int_infor[0][0]] = int_infor[0][1]
        device_if_dict[ip] = one_dict
    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(get_int('25.38.21.254', '25.38.21.199', username='admin', password='admin'), indent=4)

