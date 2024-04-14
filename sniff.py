#!/usr/bin/env python3

import subprocess

if __name__ == "__main__":
    for c in "Hello, World!":
        print(c, end="")
    print()

    subprocess.call("echo")

