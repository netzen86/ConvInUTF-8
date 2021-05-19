#!/usr/bin/python3
from sys import argv

def decuniescseq(infile):
    convert = []
    with open(infile, encoding='utf-8') as f:
        for line in f:
            line = line.encode("unicode_escape").replace(b'\\\\u', b'\\u').decode("unicode_escape")
            convert.append(line)



if __name__ == "__main__":
    outfile = argv[1]

    f = open(outfile, 'w')
    f.writelines(convert)
    f.close()
    
    f = open(convOutfile, 'r')
    print(f.read())