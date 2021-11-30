import paramiko
import time


def sshconfig(ip,username, password, brand ,cmd):
    # 实例化SSHClient
    client = paramiko.SSHClient()
    # 自动添加策略，保存服务器的主机名和密钥信息
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接SSH服务端，以用户名和密码进行认证
    client.connect(hostname=ip, port=22, username=username, password=password, look_for_keys=False)
    chan = client.invoke_shell()
    time.sleep(2)
    chan.settimeout(9000)
    chan.send("\n")#登录之后先打一下回车
    time.sleep(1)
    chan.send("\n")  # 登录之后先打一下回车
    time.sleep(1)
    comform = 'Continue'
    comform1= 'choose'
    # 获取登陆后的消息

    welcomeinfo = chan.recv(9999).decode()
    if (comform in welcomeinfo) | (comform1 in welcomeinfo):
        chan.send("n"+'\n')

    if brand.lower()=='h3c':
        chan.send('screen-length dis' + '\n')
    elif brand.lower()=='huawei':
        chan.send('screen-length 0 temporary' + '\n')
    elif brand.lower()=="cisco":
        chan.send('terminal length 0'+'\n')


    time.sleep(2)
    chan.send(cmd + '\n')
    time.sleep(5)
    result = ''
    enterMsg = 'Press Enter to continue'
    #  循环获取数据
    result = chan.recv(9999999).decode()
    result=result.split('version', 1)[-1]
    client.close()#很重要
    # print result
    # print type(result)
    return result


if __name__ == '__main__':
    print(sshconfig('172.17.1.3', 'admin', 'H3c.com!123', 'h3c', 'dis ip int brief'))
    # print(sshconfig('192.168.56.100', 'admin', 'admin', 'huawei', 'dis ip int brief'))
