"""
Copyright July 23, 2020 Aymeric Pallottini
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from core.log import logging, LOG_PREFIX, log_traceback
import subprocess
import shlex
import ConfigParser as configparser
from configuration import InstallPath
    

@log_traceback
def getdest(dest,log=logging.getLogger("{}.send_to_signal".format(LOG_PREFIX))):
    parser = configparser.ConfigParser()
    parser.read(InstallPath+'/services/signal-cli.cfg')
    dest_dict = {section: dict(parser.items(section)) for section in parser.sections()}
    log.debug(dest_dict)
    destnb=dest_dict['signal-cli'][dest]
    return destnb

@log_traceback
def send_to_signal(message,dest,log=logging.getLogger("{}.send_to_signal".format(LOG_PREFIX))):
    """
    send_to_signal(message,dest,log=logging.getLogger("{}.send_to_signal".format(LOG_PREFIX)))

    Send message to signal via signal-cli
    requires installation and configuration 
    of signal-cli before use
    https://community.openhab.org/t/setup-open-whisper-systems-signal-messenger-for-use-with-oh2-via-scripts/38103


    requires openhab2 install path in configuration.py:
    InstallPath = "/etc/openhab2"

    message is a string
    dest is a string
    
    dest are configured through config file in services folder
    format is:
    [signal-cli]
    dest=phonenb
    dest2=-g groupID
    """


    destnb = getdest(dest)
    log.debug(destnb)
    cmd='/usr/local/bin/signal-cli --config /var/lib/signal-cli -u +393465804890 send -m "' + message + '" ' + destnb
    log.debug(cmd)
    try:
        process = subprocess.call(shlex.split(cmd))
        log.info("message sent to: "+ dest + " Content: " + message)
    except:
        log.warn("message could not be sent to: "+ dest + 
                " Content: " + message +
                "\n  Check signal-cli is installed and services/signal-cli.cfg is setup")
