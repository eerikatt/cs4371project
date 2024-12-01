# HMAC response system

This repository contains the code for the intrusion response system based on the intrusion 
detection system from [1]. The code is compatible with any IDS system and includes a proposed
authentication system using hash-based message authentication codes (HMAC).

**<p align="center">Figure 1: The overview of the HMAC response system model.</p>**
<p align="center">
<img src="https://github.com/eerikatt/cs4371project/blob/main/figure1.jpeg" width="700" />
</p>

## Implementation 
### Dataset
CICIDS2017 dataset. This dataset contains generated network traffic including packets where a cyber-attack was detected.
* Available at: https://www.unb.ca/cic/datasets/ids-2017.html
* A sample of this dataset is included in the provided code.

### Hash-Based Message Authentication Code (HMAC)
HMAC is a mechanism used to 

### Packet Capture
* The default IP address in this repository is '127.0.0.1'.
* The default port address in this repository is '8080'.

Wireshark was used to view any captured packets. To view these packets using the default IP address and port,
set the capture setting to "Loopback: lo0", and apply the UDP filter.

To use the program over a Wifi connection, change the IP address in the sender and receiver functions to the desired address.
Change the capture setting to "Wi-Fi: en0". Once that is done, the UDP filter needs to be applied. If needed, change the 
port number in Wireshark settings or by using the filter udp.port=='PORT', where 'PORT' is the desired port number.



### Requirements and Libraries
* Python
* hashlib
* pandas
* hmac
* socket
* Wireshark ( Any other packet capture tool can be used. )


## Acknowledgements
* [1] L. Yang, A. Moubayed, and A. Shami, “MTH-IDS: A Multi-Tiered Hybrid Intrusion Detection System for Internet of Vehicles,” 
IEEE Internet of Things Journal, vol. 9, no. 1, pp. 616-632, Jan.1, 2022, doi: 10.1109/JIOT.2021.3084796.
