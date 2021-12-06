from netmiko import ConnectHandler as ch
import argparse


def qx_multi_cmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    host = {
        'device_type': 'hp_comware',
        'host': ip,
        'username': username,
        'password': password,
        'port': 22
    }
    conn = ch(**host)
    output = conn.send_config_set(cmd_list)
    return output


if __name__ == '__main__':

    print(qx_multi_cmd(ip='172.17.1.3', username='admin', password='H3c.com!123', cmd_list='dis cu'))

