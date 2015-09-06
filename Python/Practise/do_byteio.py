# -*- coding: utf-8 -*-

from io import BytesIO

# write to BytesIO
f = BytesIO()
f.write(b'Hello')
f.write(b' ')
f.write(b'world!\n')
print(f.getvalue())

# read from BytesIO
data = '好好学习，天天向上！'.encode('utf-8')
fread = BytesIO(data)
print(f.read())