#!/usr/bin/env python3

import subprocess

def hello():
    for c in "Hello, World!":
        print(c, end="")


if __name__ == "__main__":
    hello()
    print()

    returncode = subprocess.call(["echo", "Hello,", "World?!"])
    print(returncode)

    exit(-1)

