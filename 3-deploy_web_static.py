#!/usr/bin/python3
"""
Distribute archive to web servers
"""
from fabric.api import *
import os
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['18.210.14.235', '100.25.16.27']
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """
        pack web_static folder into a .tgz archive
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time)
    archive_path = "versions/{}".format(archive_name)

    local("mkdir -p versions")

    result = local("tar -czvf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    return None


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

def deploy():
    """
    Pack tarball and deploy to servers web-01 and web-02
    """
    filepath = do_pack()
    if not filepath:
        return False
    return do_deploy(filepath)
