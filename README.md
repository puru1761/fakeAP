# Fake Wifi Access Point Creator

Create your own wifi access point because you can!

## Usage

Make the python file executable and run it as follows:

```
$ chmod +x fakeAP.py
$ ./fakeAP.py -i INTERFACE [--ssid SSID]
```

For example:

```
$ ./fakeAP.py -i wlan0mon --ssid TestAP
[I] INFO: Beacon Frame created with SSID: 'TestAP'
[I] INFO: Transmitting Beacon through interface 'wlan0mon'

Press Enter to start Access Point 'TestAP'

[+] SUCCESS: Access Point Created!
.................................................................................
```

To view the help:
```
./fakeAP.py -h
usage: fakeAP.py [-h] -i INTERFACE [--ssid SSID]

[X] Fake Wifi Access Point Creator [X]

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Name of the interface to be used
  --ssid SSID           Name for your fake access point

[*] Author: 0xBADB01
```

## Author

* Puru
* pkulkar6@jhu.edu
