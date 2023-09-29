#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
            If number is 0 or 1, keeps only the most recent archive. If
            number is 2, keeps the most and second-most recent archives, etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Cleaning local archives
    local_archives = sorted(os.listdir("versions"))
    [local_archives.pop() for i in range(number)]
    with lcd("versions"):
        [local(f"rm ./{a}") for a in local_archives]

    # Cleaning remote archives
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        [remote_archives.pop() for i in range(number)]
        [run(f"rm -rf ./{a}") for a in remote_archives]
