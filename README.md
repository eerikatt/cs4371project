# HMAC response system

This repository contains the code for the intrusion response system based on the intrusion 
detection system from [1]. The code is compatible with any IDS system and includes a proposed
authentication system using hash-based message authentication codes (HMAC).

**<p align="center">Figure 1: The overview of the HMAC response system model.</p>**
<p align="center">
<img src="https://github.com/eerikatt/cs4371project/blob/main/figure1.jpeg" width="700" />
</p>

## Implementation 

### Cloning the Repository


To clone the repository, use the following command : git clone https://github.com/eerikatt/cs4371project

### Dataset
CICIDS2017 dataset. This dataset contains generated network traffic including packets where a cyber-attack was detected.
* Available at: https://www.unb.ca/cic/datasets/ids-2017.html
* A sample of this dataset is included in the provided code.

### Hash-Based Message Authentication Code (HMAC)
HMAC is a mechanism used to verify the authenticity and and integrity of a message. A message authenitcation code is a code calculated from a message and either sent or stored with it in order for the receiver to verify the message. HMAC uses a hash algorithm such as SHA-256 to calculate this code. The receiver of this message shares a secret key with the sender in order to verify the message. The receiver uses the secret key and the hash algotrithm to compute the HMAC of the message. If the computed HMAC matches with the received HMAC, the message is verified as genuine. Some researchers have created other HMAC authentication programs to be used with the Local Interconnect Networks bus. [2]

### Packet Capture
* The default IP address in this repository is '127.0.0.1'.
* The default port address in this repository is '8080'.

Wireshark was used to view any captured packets. To view these packets using the default IP address and port,
set the capture setting to "Loopback: lo0", and apply the UDP filter.

To use the program over a Wifi connection, change the IP address in the sender and receiver functions to the desired address.
Change the capture setting to "Wi-Fi: en0". Once that is done, the UDP filter needs to be applied. If needed, change the 
port number in Wireshark settings or by using the filter udp.port=='PORT', where 'PORT' is the desired port number.

Once capture settings are set up, once the sender and reicever functions are run, you will be able to see the packets being sent and received.

Without HMAC implementation, packets containing attacks are captured:

With HMAC implementatin, only packets considered safe are captures, along with their HMAC.

**<p align="center">Figure 2: Packets captured with HMAC.</p>**
<p align="center">
<img src="https://github.com/eerikatt/cs4371project/blob/main/figure2.png" width="800" />
</p>



### Requirements and Libraries
* Python
* json
* hashlib
* pandas
* hmac
* socket
* Wireshark ( Any other packet capture tool can be used. )


## Acknowledgements
* [1] L. Yang, A. Moubayed, and A. Shami, “MTH-IDS: A Multi-Tiered Hybrid Intrusion Detection System for Internet of Vehicles,” 
IEEE Internet of Things Journal, vol. 9, no. 1, pp. 616-632, Jan.1, 2022, doi: 10.1109/JIOT.2021.3084796.

* [2] F. Páez and H. Kaschel, "A Proposal for Data Authentication, Data Integrity and Replay Attack Rejection for the LIN Bus," 2021 IEEE CHILEAN Conference on Electrical, Electronics Engineering, Information and Communication Technologies (CHILECON), Valparaíso, Chile, 2021, pp. 1-7, doi: 10.1109/CHILECON54041.2021.9702979.
