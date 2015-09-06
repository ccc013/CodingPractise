# -*- coding: utf-8 -*-

# 使用subprocess模块启动子进程，然后控制其输入和输出
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 子进程需要输入，可以通过communicate（）方法输入:
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8','ignore'))
print('Exit code:', p.returncode)
