# file: openpage.py
#
# author: Eric Miers
# version: 10/15/2018
#
# desc: Opens page passed in from handler.py

import os
import sys
import time
import subprocess
import webbrowser
from urllib.request import pathname2url


def openPage(page):

    """ Opens page passed in by handler; closes after 30s

    Args:
        page: path string to page

    Returns:
        200 code if successful, 400 if unsuccessful

    """
    if (os.path.isfile(page)):
        url = 'file:{}'.format(pathname2url(os.path.abspath(page)))
        browser = subprocess.Popen(['firefox', url], start_new_session=True)
        time.sleep(30)
        browser.terminate()
    else:
        print("ERROR: File could not be opened")
        return 400

    return 200

if __name__ == '__main__':
    openPage(sys.argv[1])
