#!/usr/bin/python3
"""
Pack tarball and deploy to servers
"""
from fabric.api import *


do_pack = __import__('1-pack_web_static')
do_deploy = __import__('2-do_deploy_web_static')
env.hosts = ["54.144.131.244", "52.91.128.208"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def deploy():
    """
    Pack tarball and deploy to servers web-01 and web-02
    """
    filepath = do_pack.do_pack()
    if not filepath:
        return False
    return do_deploy.do_deploy(filepath)
