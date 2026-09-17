# Plan

Laptop (simulated exchange)
 - Test packet generator (someway to generate test market data and wrap as UDP packets)
 - Ethernet sender (send generated UDP packets via ethernet to Arty)

FPGA
 - PHY interface 
 - Ethernet receive
 - Clock domain crossing
 - Packet parser
 - Filter (to only keep packets that are "real" market data)
 - Queue (to hold results until UART can push)
 - Formatter (ensure data is formatted correctly as bytes)
 - UART transmitter (send packets via USB back to host/laptop)
 
 Laptop (simulated host)
 - Serial receiver (receive UART stream)
 - Logger (split stream into entires, decode, and save log)
 - Checker (optional - automatically check logged stream against generated packets from simulated exchange)