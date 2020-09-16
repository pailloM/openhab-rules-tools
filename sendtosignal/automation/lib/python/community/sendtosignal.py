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
from configuration import signalconf, signal_secret_path


@log_traceback
def send_to_signal(message,dest,log=logging.getLogger("{}.send_to_signal".format(LOG_PREFIX))):
    """
    send_to_signal(message,dest,log=logging.getLogger("{}.send_to_signal".format(LOG_PREFIX)))

    Send message to signal via signal-cli
    requires installation and configuration 
    of signal-cli before use
    signal secret path is stored in configuration.py
    with string signal_secret_path:
    signal_secret_path='path_to_secret' (ex:'/var/lib/signal-cli')
    https://community.openhab.org/t/setup-open-whisper-systems-signal-messenger-for-use-with-oh2-via-scripts/38103


    message is a string
    dest is a string
    
    dest are configured through dictionnary in
    configuration.py signalconf
    format is:
    signalconf= {'name1': '+1xxxxxxxx',
            'name2': '+1xxxxxxx',
            'groupname': '-g groupID'}
    """

    try:
        destnb = signalconf[dest]
        log.debug(destnb)
    except:
        log.warn("Destinary not found in configuration.py signalconf")
        exit(1)
    cmd=('/usr/local/bin/signal-cli --config '+ 
                signal_secret_path + ' -u +393465804890 send -m "' + 
                message + '" ' + destnb)
    log.debug(cmd)
    try:
        output = subprocess.check_output(shlex.split(cmd))
        log.debug(':'+str(output)+':')
        output=''.join(e for e in str(output) if e.isalnum())
        if output.isdigit():
            log.info("message sent to: "+ dest + " Content: " + message)
        else:
            log.warn("message could not be sent to: "+ dest + 
                " Content: " + message +
                "\n  Check /var/lib/signal-cli is setup and accessible")

    except:
        log.warn("message could not be sent to: "+ dest + 
                " Content: " + message +
                "\n  Check signal-cli is installed and services/signal-cli.cfg is setup")
