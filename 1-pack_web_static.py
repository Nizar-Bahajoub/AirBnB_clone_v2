#!/usr/bin/python3
"""
    fabric file
"""
from fabric.api import *
from datetime import datetime


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
