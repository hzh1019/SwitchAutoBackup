from netmiko import ConnectHandler
from netmiko.ssh_exception import  NetMikoAuthenticationException, NetMikoTimeoutException
import threading
import datetime
import queue
import re, os

def conn_info(ip):
    dev = {
        'device_type': 'huawei_telnet',
        'host': ip,
        'username':'admin',
        'password': 'TJuOO8Uz',
    }
    return dev
 
def conn_dev(dev_q):
    while not dev_q.empty():  #读取队列获得每一台交换机的IP
        dev_ip = dev_q.get()
        try:
            dev_conn = ConnectHandler(**conn_info(dev_ip))
            print("[%s] Connected." % dev_ip)
 
            dev_conn.send_config_from_file('cmds.txt')  #将写好的命令行逐条写入交换机

 
            dev_conn.disconnect()
            print('[%s] done.\n' % dev_ip )
 
        except NetMikoAuthenticationException:
            print("[%s] Error! Please check username or password ..." % dev_ip)
        except NetMikoTimeoutException:
            print("[%s] Error! Connect time out ..." % dev_ip)
        except Exception as e:
            print('[%s] Error:%s' % (dev_ip, e))
 

if __name__ == "__main__":
    #交换机的IP地址列表，也可以读取文件（txt/excel/...）来获取
    devs_ip = ['192.168.12.34','192.168.12.35','192.168.13.19']
    
    devs_q = queue.Queue()
    for dev in devs_ip:
        devs_q.put(dev)
 
    max_conn = 15 # 同时操作交换机数量（可增加或减少）
    
    ts = []  # 线程集合
    for i in range(max_conn):
        t = threading.Thread(target=conn_dev, args=(devs_q,))
        t.start()
        ts.append(t)
    for t in ts:
        t.join()
 
    print("Done.")