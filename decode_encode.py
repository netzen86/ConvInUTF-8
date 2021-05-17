#!/usr/bin/python3

convInfile, convOutfile = input('Enter in file and out file names for converting: ').split()
convert = []
with open(convInfile, encoding='utf-8') as f:
    for line in f:
        line = line.encode("unicode_escape").decode("utf-8")
        if line:
            convert.append(line)

f = open(convOutfile, 'w')
rescon = "\n".join(convert).replace("\n", "")
f.writelines(rescon)
f.close()

f = open(convOutfile, 'r')
print(f.read())