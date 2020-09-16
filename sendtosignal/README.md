# Send to Signal

This library consists of a simple library that send a message through signal-cli

send_to_signal(message,dest,log=logging.getLogger("{}.send_to_signal".format(LOG_PREFIX)))


Send message to signal via signal-cli requires installation and configuration of signal-cli before use:
https://community.openhab.org/t/p-open-whisper-systems-signal-messenger-for-use-with-oh2-via-scripts/38103


message is a string
dest is a string

dest are configured through dictionnary in
configuration.py signalconf
format is:
signalconf= {'name1': '+1xxxxxxxx',
        'name2': '+1xxxxxxx',
        'groupname': '-g groupID'}



# Example

```python
from community.sendtosignal import send_to_signal
...

    # Inside a Rule send a message to a phone nb or group:
    send_to_signal("message string","dest")
```
