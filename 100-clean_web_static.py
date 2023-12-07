#!/usr/bin/python3
"""
Deletes aut-of-date archives
"""
import os
from fabric.api import *


env.hosts = ["54.144.131.244", "52.91.128.208"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_clean(number=0):
    """Function to be executed"""

    number = int(number)
    if number == 0:
        number = 1
    with lcd('versions'):
        local('ls -t | tail -n +%d | xargs rm -rf' % (number + 1))

    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +%d | xargs rm -rf' % (number + 1))
