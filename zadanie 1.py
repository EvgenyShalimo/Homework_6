s = b'r\xc3\xa9sum\xc3\xa9'
b = s.decode('utf-8')
print(b)
b = b.encode('Latin1')
print(b)
b = s.decode('utf-8')
print(b)