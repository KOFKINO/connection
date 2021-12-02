import paramiko
import argparse


def ssh_connect(ip, username='root', password='Echo3845185765', cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    usage = 'python ssh.py -i ipaddr -u username -p password -c command'
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('-i', '--ipaddr', dest='ip', help='\nssh server', default='120.27.210.240')
    parser.add_argument('-u', '--username', dest='username', help='\nssh username', default='root')
    parser.add_argument('-p', '--password', dest='password', help='\nssh password', default='Echo3845185765')
    parser.add_argument('-c', '--command', dest='cmd', help='\nshell command', default='ls')
    args = parser.parse_args()
    print(ssh_connect(args.ip, args.username, args.password, args.cmd))

    # print(ssh_connect(ip='120.27.210.240', username='root', password='Echo3845185765', cmd='pwd'))
    # print(ssh_connect(ip='', username='root', password='', cmd='pwd'))
