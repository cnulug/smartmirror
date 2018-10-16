# file: handler.py
#
# author: Eric Miers
# version: 10/15/2018
#
# desc: handles voice commands

import speech_recognition as sr
import os

# Used to reach out to wit.ai speech recognition api
WIT_API_KEY = "UKC7ERIBAXWLSARARG7P7IXP3U22LYNI"

def main():
    """ process voice commands until proper exit command passed"""
    r = sr.Recognizer()
    mic = sr.Microphone()

    status = "run"
    print("LISTENING:")
    while (status == "run"):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        command  = r.recognize_wit(audio, WIT_API_KEY)
        print("RECEIVED COMMAND: " + command)

        if (command == "maintenance exit"):
            status = exit

        status = commandHandler(command)
        print("COMMAND RETURNED WITH STATUS: " + status)

# Process speech command and call appropriate fucntion
def commandHandler(command):
    """ Determines which page should be opened based on command.
        Runs page-opener script

    Args:
        command: text conversion of vocie command

    Returns:
        20x code if successful, 200 if unhandleable, 400 if unsuccessful

    """

    try:
        # Will open commands_list.html
        if ("list of commands" in command or "command" in command):
            page = "../../display_pages/pages/commands_list.html"
            runScript = "python3 openpage.py " + page
            os.system(runScript)
            return 201

        """ ADD NEW CASES HERE """

    except:
        print("ERROR: Cannot spawn page-opener")
        return 400

    return 200

if __name__ == '__main__':
    main()
