#!/usr/bin/env python3

import subprocess
import sys
import json
import xmltodict

host = sys.argv[1]
out_file = "out.xml"

out_bytes = subprocess.check_output(["nmap", "-oX", out_file, host])

f = open(out_file)
xml_content = f.read()
f.close()

nmap_results = xmltodict.parse(xml_content)
#print(json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True))

data = []
try:
    for port in nmap_results['nmaprun']['host']['ports']['port']:	
        data.append({ 
            "port": port['@portid'],
            "protocol": port['@protocol'],
            "state": port['state']['@state'],
            "service-name": port['service']['@name'] 
        })
except KeyError: # no open ports
    pass

print(json.dumps(data, indent=4, sort_keys=True))
