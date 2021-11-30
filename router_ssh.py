from netmiko import ConnectHandler as ch


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
    print(output)


if __name__ == '__main__':
    cmd_list = ['dis version', 'ospf 1', 'area 0', 'net 192.168.56.100 0.0.0.255']
    qx_multi_cmd(ip='192.168.56.100', username='admin', password='admin', cmd_list=cmd_list)
