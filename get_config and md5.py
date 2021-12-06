from router_ssh import qx_multi_cmd
import re
import hashlib
import sqlite3
import time


def get_config_and_md5(ip, username, password):
    run_config = qx_multi_cmd(ip, username, password, 'dis cu')
    time.sleep(5)
    run_config_split = re.split(r'\r\n S|sysname\s+\S+', run_config)
    config = run_config.replace(run_config_split[0], '').strip()
    m = hashlib.md5()
    m.update(config.encode())
    config_md5 = m.hexdigest()

    return config, config_md5


def write_config(device_list, username, password):
    conn = sqlite3.connect('config_sql.sqlite')
    cursor = conn.cursor()

    for device in device_list:
        config_and_md5 = get_config_and_md5(device, username, password)
        cursor.execute('select config_md5 from config where ip = '+"'" + device + "'" )
        # cursor.execute('select config_md5 from config where ip = ?', (device,))
        result = cursor.fetchall()
        if not result:
            cursor.execute('insert into config (ip, config, config_md5) values (? ,? ,?)',
                           (device, config_and_md5[0], config_and_md5[1]))
            conn.commit()
            print('新增' + device + '配置文件')
        if result:
            if result[0][0] == config_and_md5[1]:
                print(device + '配置已存在，未修改')
                continue
            if result[0][0] != config_and_md5[1]:
                cursor.execute('update  config  set config = ?, config_md5 = ? where ip =?', \
                               (config_and_md5[0], config_and_md5[1], device))
                conn.commit()
                print('更新' + device + '配置及md5')
        cursor.execute('select * from config')
        all_configs = cursor.fetchall()
        print(all_configs)


if __name__ == '__main__':
    device_list = ['172.17.1.3']
    username = 'admin'
    password = 'H3c.com!123'
    write_config(device_list, username, password)
