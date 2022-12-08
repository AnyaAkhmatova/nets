#!/usr/bin/env python3.8

import platform
import subprocess
import sys


def find_mtu(host):
    left = 68 - 28
    right = 1501 - 28
    while right - left > 1:
        med = (right + left) // 2
        command = ['ping', host, '-c', '1', '-s', str(med), '-M', 'do']
        result = subprocess.run(command, capture_output=True)
        if result.returncode == 1:
            print("Error occured during finding mtu.", file=sys.stderr)
            print(result.stderr.decode('UTF-8'), file=sys.stderr)
            exit(1)
        if result.returncode == 0:
            left = med
        else:
            right = med
    return left


if len(sys.argv) != 2:
    print("One argument (host) required.", file=sys.stderr)
    exit(1)

host = sys.argv[1]

command = ['ping', host, '-c', '1', '-s', str(68 - 28), '-M', 'do']
result = subprocess.run(command, capture_output=True)
if result.returncode != 0:
    print("Error occured during first ping.", file=sys.stderr)
    print(result.stderr.decode('UTF-8'), file=sys.stderr)
    exit(1)

mtu = find_mtu(host) + 28

print('MTU = ' + str(mtu))
