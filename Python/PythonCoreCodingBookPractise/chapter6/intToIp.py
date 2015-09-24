#!/usr/bin/env python3
# -*- coding: utf-8

# int to Ip address
def intToIp(num):
	s = []
	for i in range(4):
		s.append(str(num % 256))
		num //= 256
	return '.'.join(s[::-1])

# IP address to int
def ipToInt(ips):
	s = ips.split('.')
	sum = 0
	for idx,val in enumerate(s[::-1]):
		sum += int(val) * (256 ** idx)
	return sum

# test
print('int to IP: %s' % intToIp(123456789))
print('Ip to int: %d' % ipToInt('7.91.205.21'))
# use lambda
ch2 = lambda x : '.'.join([str(x // (256 ** i) % 256) for i in range(3,-1,-1)])
print(ch2(123456789))

# IP address to int using lambda
ch3 = lambda x : sum([256 ** j * int(i) for j,i in enumerate(x.split('.')[::-1])])
print(ch3('7.91.205.21'))
