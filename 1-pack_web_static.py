#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from the contents of web_static.
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """
    Generates a tgz archive of the web_static directory.
    Returns the path to the created archive or None on failure.
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(current_time)
        archive_path = "versions/{}".format(archive_name)

        if not isdir("versions"):
            local("mkdir -p versions")

        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        print("An error occurred: {}".format(e))
        return None
