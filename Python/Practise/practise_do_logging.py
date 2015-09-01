# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

# 使用logging，输出：
# INFO:root:n = 0
# Traceback (most recent call last):
#   File "practise_do_logging.py", line 9, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
