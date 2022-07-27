#!/usr/bin/python3

friends = {'tom': '111-222-333', 'jerry': '666-33-111'}

print(friends)

friends['bob'] = '888-999-666'

print(friends)

friends['jerry'] = '666-333-111'

print(friends)

print(friends['bob'])

print(friends)

del friends['jerry']

print(friends)
