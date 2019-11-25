# SwitchAutoBackup
 H3C 交换机批量备份

### 开发背景
公司内部署有200多台H3C交换机，为保障交换机因故障替换时及时恢复网络，特编写此脚本每日备份交换机配置至tftp服务器，备份文件名格式为: ip-日期.bak.cfg,ip内的"."用"-"替代，如：192-168-29-1-20191111.bak.cfg

### 环境需求
1. 一台具备python3 执行环境的机器
2. 一台tftp服务器
3. 被管理交换机已开启Telnet登陆，并设置相应的用户和密码及执行backup命令的权限
### 使用方法
1. 将Switch_AutoBackup.py与switchs.txt放在同一目录内
2. 编辑Switch_AutoBackup.py，填入本地环境相应的信息
```
#交换机具备backup命令的telnet用户
        username = 'admin'
        #该用户密码
        password = 'admin'
        #tftp服务器地址
        ftphost ='192.168.32.11'
```
3. 编辑switchs.txt，填入需要备份配置的交换机管理ip地址，每行一台
```
192.168.29.1
192.168.29.10
```
4. 根据自己的需求将如下命令设置为Windows或Linux计划任务
```
python3 Switch_AutoBackup.py
```

## Telnet代码源自网络，前人栽树，后人乘凉，感谢！
