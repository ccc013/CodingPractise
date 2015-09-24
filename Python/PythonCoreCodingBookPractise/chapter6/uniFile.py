#!usr/bin/env python
# -*- coding: utf-8 -*-

'''
An example of reading and writing Unicode string:Writes
a Unicode string to a file in utf-8 and reads it back in.
'''

CODEC='utf-8'
FILE='unicode.txt'

hello_out = u"Hello python!\n"
bytes_out = hello_out.encode(CODEC)
# write to file in utf-8
f = open(FILE,'w')
f.write(bytes_out)
f.close()

# read
fr = open(FILE,'r')
bytes_in = fr.read()
fr.close()
hello_in = bytes_in.decode(CODEC)
print hello_in