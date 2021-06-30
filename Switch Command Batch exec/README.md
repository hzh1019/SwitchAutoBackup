# Switch Command Batch exec
批量执行交换机命令

### 开发背景
多台华为、H3C网络设备需进行配置变更，比如：更改密码、配置ntp服务器。使用该脚本提高效率。

### 环境需求
1. 一台具备python3 执行环境的机器
2. 安装netmiko组件
3. 被管理交换机已开启Telnet登陆，并设置相应的用户和密码及执行相应命令的权限

### 使用方法
1. 将switch_command.py与cmds.txt放在同一目录内
2. 编辑switch_command.py，填入本地环境相应的信息
```
#交换机登录方式及用户名和密码
        'device_type': 'huawei_telnet',
        'username':'admin',
        'password': 'TJuOO8Uz',

#交换机的IP地址列表，也可以读取文件（txt/excel/...）来获取
    devs_ip = ['192.168.12.34','192.168.12.35','192.168.13.19']
```

3. 编辑cmds.txt，填入需执行的命令
```
sys
……
save f
```
## 脚本调用netmiko组件，可支持Cisco等其他主流设备，详情请至https://github.com/ktbyers/netmiko 查阅。

## 执行前请先进行测试！执行前请先进行测试！执行前请先进行测试！
