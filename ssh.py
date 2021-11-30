import paramiko
import sys


def ssh_connect(ip, username, password, port=22, cmd='dis cu'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    print(x, flush=True)


if __name__ == '__main':
    # ssh_connect(ip='192.168.56.100', username='admin', password='admin', cmd='dis int brief')
    print(ssh_connect(ip='120.27.210.240', username='root', password='Echo3845185765', cmd='pwd'))
