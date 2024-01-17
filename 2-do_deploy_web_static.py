#!/usr/bin/python3
"""
Distribute archive to web servers
"""
from fabric.api import put, run, env
import os


env.user = 'ubuntu'
env.hosts = ['18.210.14.235', '100.25.16.27']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distribute archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    tmp_tar = "/tmp/{}".format(filename)
    name, ext = os.path.splitext(filename)
    new_folder = "/data/web_static/releases/{}".format(name)
    try:
        put(archive_path, tmp_tar)
        run("mkdir -p {}".format(new_folder))
        run("tar -xzf {} -C {}".format(tmp_tar, new_folder))
        run("rm {}".format(tmp_tar))
        run("mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("rm -rf {}/web_static".format(new_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False
