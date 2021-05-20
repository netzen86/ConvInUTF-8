#!/usr/bin/python3
from sys import argv
from sys import exit
import subprocess 

def decuniescseq(infile):
    dectxt = []
    with open(infile, encoding='utf-8') as f:
        for line in f:
            line = line.encode("unicode_escape").replace(b'\\\\u', b'\\u').decode("unicode_escape")
            dectxt.append(line)
    return dectxt

def encescseq(infile):
    enctxt = []
    with open(infile, encoding='utf-8') as f:
        for line in f:
            line = line.encode("unicode_escape").decode("utf-8").replace("\\n", "\n")
            enctxt.append(line)
    return enctxt




if __name__ == "__main__":
    try:
        action = argv[1]
        inputf = argv[2]
        outputf = argv[3]
    except IndexError:
        print("Run script with this args:\nAction - decode | encode; input file; output file")
        exit(1)

    print(f'\n*** {inputf} is backuped ***\n')
    subprocess.run(['cp', inputf, inputf + '.bak'])    
    
    f = open(outputf, 'w')
    if "decode" in action:
        f.writelines(decuniescseq(inputf))
    elif "encode" in action:
        f.writelines(encescseq(inputf))

    f.close()
    f = open(outputf, 'r')
    print(f.read())