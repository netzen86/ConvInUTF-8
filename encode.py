#!/usr/bin/env python

convInfile, convOutfile = input('Enter in file and out file names for converting: ').split()
convert = [] 
with open(convInfile, encoding='utf-8') as f:
    for line in f:
        line = line.encode("unicode_escape").replace(b'\\\\u', b'\\u').decode("unicode_escape")
        if line:
            convert.append(line)

f = open(convOutfile, 'w')
f.writelines(convert)
f.close()

f = open(convOutfile, 'r')
print(f.read())