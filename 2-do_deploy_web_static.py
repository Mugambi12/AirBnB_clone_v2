#!/usr/bin/python3
"""
Fabric script to distribute an archive to a web server.
"""

import os.path
from fabric.api import env, put, run

# Define the target servers
env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        False if the file doesn't exist at archive_path or an error occurs, otherwise True.
    """
    if not os.path.isfile(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    name = os.path.splitext(file_name)[0]

    # Upload the archive
    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False

    # Extract and deploy
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed or \
       run("mkdir -p /data/web_static/releases/{}/".format(name)).failed or \
       run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, name)).failed or \
       run("rm /tmp/{}".format(file_name)).failed or \
       run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed or \
       run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed or \
       run("rm -rf /data/web_static/current").failed or \
       run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
        return False

    return True
