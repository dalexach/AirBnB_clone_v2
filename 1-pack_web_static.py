#!/usr/bin/python3
"""
    Script to generate a .tgz archive
"""


def do_pack():
    """
        Funtion that creates a .tgz
    """

    from datetime import datetime
    from fabric.api import local

    date_now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = "./versions/web_static_{}".format(date_now)
    local("mkdir -p ./versions")
    create = local("tar -cvzf {} web_static".format(path))

    if create.succeeded:
        return path
    else:
        return None

if __name__ == "__main__":
    do_pack()
