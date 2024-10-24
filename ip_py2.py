import os
import sys

ip_ad=str(sys.argv[1])
grep = "| grep "'"64 bytes"'
cut = "| cut -d "'" "' " -f 4"
tr = "| tr -d "'":"'
for ip in range(1,255):
    out = os.system(f"ping -c 1 {ip_ad}.{ip} {grep} {cut} {tr}")
    print(out)
