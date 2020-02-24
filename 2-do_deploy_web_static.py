#!/usr/bin/python3
"""
    Script to generate a .tgz archive
"""


from datetime import datetime
from fabric.operations import local, run, put, env
import os
import re


env.hosts = ['34.74.41.230', '34.74.9.120']
env.user = 'ubuntu'

def do_pack():
    """
        Funtion that creates a .tgz
    """

    date = datetime.now()
    date_now = date.strftime("%Y%m%d%H%M%S")

    try:
        if not os.path.isdir("versions"):
            local("mkdir versions")

        f1 = "versions/web_static_{}.tgz web_static".format(date_now)
        f2 = local("tar -cvzf {}".format(f1))
        return f2

    except Exception:
        return None

def do_deploy(archive_path):
    """
    	Function to deploy
    """

    if not os.path.exists(archive_path):
        return False

    tar_name = re.search('web_static_[0-9]*.tgz', archive_path).group(0)
    untar_path = "/data/web_static/releases/{}"\
        .format(tar_name.replace('.tgz', ''))

    put(archive_path, '/tmp')
    run("mkdir -p {}".format(untar_path))
    run("tar -zxf /tmp/{} -C {}".format(tar_name, untar_path))
    run("rm /tmp/{}".format(tar_name))
    run("mv {}/web_static/* {}".format(untar_path, untar_path))
    run("rm -rf {}/web_static".format(untar_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(untar_path))
    print("New version deployed!")
