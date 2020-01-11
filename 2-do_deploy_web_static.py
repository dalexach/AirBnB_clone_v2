#!/usr/bin/python3
"""
    Script to generate a .tgz archive
"""

from datetime import datetime
from fabric.api import local
import os

env.hosts = ['34.74.41.230', '34.74.9.120']
env.user = 'ubuntu'

def do_pack():
    """
        Funtion that creates a .tgz
    """

    date_now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = "./versions/web_static_{}".format(date_now)
    local("mkdir -p ./versions")
    create = local("tar -cvzf {} web_static".format(path))

    if create.succeeded:
        return path
    else:
        return None

def do_deploy(archive_path):
    """
    	Function to deploy
    """

    if not os.path.exists(archive_path):
        return False
    if not put(archive_path, "/tmp/").succeeded:
        return False
    print("Hello")
    file_name = archive_path[9:]
    folder_name = "/data/web_static/releases/" + file_name[:-4]
    file_name = "/tmp/" + file_name
    if not run('mkdir -p {}'.format(folder_name)).succeeded:
        return False
    if not run('tar -xzf {} -C {}'.format(file_name, folder_name)).succeeded:
        return False
    if not run('rm {}'.format(file_name)).succeeded:
        return False
    if not run('mv {}/web_static/* {}'.format(folder_name,
                                              folder_name)).succeeded:
        return False
    if not run('rm -rf {}/web_static'.format(folder_name)).succeeded:
        return False
    if not run('rm -rf /data/web_static/current').succeeded:
        return False
    return run('ln -s {} /data/web_static/current'.format(
        folder_name)).succeeded
