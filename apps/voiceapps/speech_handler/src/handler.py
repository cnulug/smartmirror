# file: handler.py
#
# author: Eric Miers
# version: 10/15/2018
#
# desc: handles voice commands

import speech_recognition as sr
import os
import threading
import subprocess
from urllib.request import pathname2url

# Used to reach out to wit.ai speech recognition api
WIT_API_KEY = "UKC7ERIBAXWLSARARG7P7IXP3U22LYNI"
INIT = 100
EXIT = 500

def main():
    """ process voice commands until proper exit command passed"""
    r = sr.Recognizer()
    mic = sr.Microphone()

    voiceListener(r, mic)


def voiceListener(r, mic):

    status = INIT
    print("LISTENING:")
    while (status != EXIT):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        command  = r.recognize_wit(audio, WIT_API_KEY)
        print("RECEIVED COMMAND: " + command)

        if (command == "maintenance exit"):
            status = EXIT

        commandHandler(command)

# Process speech command and call appropriate fucntion
def commandHandler(command):
    """ Determines which page should be opened based on command.
        Runs page-opener script

    Args:
        command: text conversion of voice command

    Returns:
        20x code if successful, 200 if unhandleable, 400 if unsuccessful

    """

    try:
        # Will open commands_list.html
        if ("list of commands" in command or "command" in command):
            page = "../../display_pages/pages/commands_list.html"
            openPage(page)

            return 201

        """ ADD NEW CASES HERE """

    except Exception as e:
        print("ERROR: Cannot spawn page-opener")
        print(e)
        return 400

    return 200

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
    else:
        print("ERROR: File could not be opened")
        return 400

    return 200



if __name__ == '__main__':
    main()
