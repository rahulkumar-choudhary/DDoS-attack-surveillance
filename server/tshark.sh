#!/bin/zsh


# run on the server of hosted application.
# Note: Run from root user
# Example: sudo ./tshark.sh


# get the network interface:
# tshark -D

networkInterface=ens4

numberOfRequest=1000
path="../test-data/"

# bug in tshark: /root/file.pcap
# ref: https://www.linuxquestions.org/questions/linux-networking-3/tshark-gives-permission-denied-writing-to-any-file-in-home-dir-650952/

# get the network log and save in ddoslog.pcap file
sudo tshark -w ../test-data/ddoslog.pcap -i ${networkInterface} -c ${numberOfRequest}

# show the output and save in csv
sudo tshark -r ../test-data/ddoslog.pcap -T fields \
    -e ip.src \
    -e ip.dst \
    -e tcp.srcport \
    -e tcp.dstport \
    -e ip.proto \
    -e frame.len \
    -e tcp.seq \
    -e tcp.ack \
    -e tcp.len \
    -E header=y -E separator=, > ${path}networkRequest.csv

# -E header=y -E separator=, -E quote=d > ${path}networkRequest.csv
# ip.src,ip.dst,tcp.srcport,tcp.dstport,ip.proto,frame.len,tcp.seq,tcp.ack,tcp.len
# "140.82.112.26","192.168.1.5","443","35398","6","92","1","1","26"

# # run python prediction file
python3 ./predict.py

# see whats in the file
# sudo tshark -r ./ddoslog.pcap


# Frame Number: 1
# Time: 0.000000000
# Source IP Address: 192.168.59.110
# Destination IP Address: 23.57.12.251
# Protocol: TCP
# Length: 66
# Source Port: 40184
# Destination Port: 443
# TCP Flags: [ACK]
# Sequence Number: 1
# Acknowledgment Number: 1
# TCP Window Size: 501
# TCP Length: 0
# Timestamps: TSval=4238852620 TSecr=4219202677

# output:
# "2","0.003089439","23.57.12.251","192.168.59.110","6","97","443","40184","0x0018","1","2","501","31","0.003089439"

