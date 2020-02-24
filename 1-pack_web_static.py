#!/usr/bin/python3
"""
    Script to generate a .tgz archive
"""

from datetime import datetime
from fabric.operations import local, run
import os


def do_pack():
    """
        Funtion that creates a .tgz
    """

    date = datetime.now()
    date_now = date.strftime("%Y%m%d%H%M%S")

    try:
        if not os.path.isdir("versions"):
            local("mkdir versions")

        f1 = "versions/web_static{}.tgz web_static".format(date_now)
        f2 = local("tar -cvzf {}".format(f1))
        return f2 

    except Exception:
        return None
