#!/usr/bin/env python3

import subprocess

if __name__ == "__main__":
    for c in "Hello, World!":
        print(c, end="")
    print()

    returncode = subprocess.call(["echo", "Hello,", "World?!"])
    print(returncode)

    exit(-1)

