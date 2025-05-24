
#  Blockchain Construction and Analysis of Consensus Algorithm:
 
Here we have constructed a blockchain with the help of python programming language. In this work we have established a peer to peer connection between n number of full nodes and further we have analysed the consensus algorithms on our blockchain system.


## Table of Contents:
- Introduction
- Features
- Installation
- Usage
- Configuration
- Contact
- Acknowledgement

## Introduction:
In this project we have constructed a basic cryptocurrency setup/model which represents how cryptocurrencies actually work at core. Further we have constructed a peer to peer system in which we can understand how mining takes place at various nodes in a blockchain and how data is transferred between nodes.
Additionally we have done analysis on the consensus algorithm proof of work(pow).

## Features:

- Full nodes: in this  setup every node is a full node and we can easily add a new node which will also be a  full node.
- Transaction poll: It store all the transaction which has to be mined later. Miner select the transaction from the transaction pool to mine. 
- Mining: Implemented basic proof of work algorithm and further study on the various difficulty levels and how difficulty level affect mining.
- Block Broadcasting: Broadcast newly created block to all the nodes in the blockchain.
- Scalability: this setup is very flexible and we can analyse different consensus on this setup easily by little bit of changes only.
- Integrity: Maintaining the immutability of the blockchain and making it consistent across all the nodes.

## Installation

- Download Install VS code from the official website.


  <https://code.visualstudio.com/download>

- Install the ___python extension___ in the VS code.
![photo](https://imgs.search.brave.com/-0CybY4nT54KhgD8lRSuJMMJgvT3bDIcQYXHwKGx5M4/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9saWdo/dHJ1bi5jb20vd3At/Y29udGVudC91cGxv/YWRzLzIwMjMvMDMv/cHl0aG9uX2Zvcl92/c2NvZGUucG5n)
- Install the required python libraries if they are not preinstalled.
  ## Libraries
- import hashlib
- import multiprocessing
- import socket  
- import json    
- from datetime import datetime
- import time
- import random
- import string
## Setup:

- Connect the systems/nodes over a network. We can do this with the help of a switch device or over the wifi.
- In the network setting of each system allow file sharing over the network and grant all the permissions.
- you can take help from the video given below 

  <https://youtu.be/CGeAauny2fc?si=Whea1SzorUv5BNm5>

- we can check if the nodes are connected by ping command and using ip address.further is also exlained in the above video.
![](https://imgs.search.brave.com/8Vw1r-0jflfNXzH1W1ctvrgzj9ZonH_GR_CeSiCbofw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9ibG9n/LmludmdhdGUuY29t/L2hzLWZzL2h1YmZz/L3BpbmctY29tbWFu/ZC1zeW50YXgtZXhh/bXBsZS0yLnBuZz93/aWR0aD02ODAmaGVp/Z2h0PTMxMCZuYW1l/PXBpbmctY29tbWFu/ZC1zeW50YXgtZXhh/bXBsZS0yLnBuZw)

- After that if any issue comes it might be a firewall issue.

## Usage:

we can just run the attached python file in vs code 

After running the code on all node add the node name and difficulty of mining. it must be noted that difficulty should be same on all the nodes

- further we can have a look what different function does in the code.

for generating random transactions
``` python
def generate_transection():
    letters = string.ascii_letters  # includes lowercase and uppercase letters
    result_str = ''.join(random.choice(letters) for _ in range(20))
    return result_str
```
for mining
``` python
def mine(block,difficulty):
    n=difficulty
    difficulty='0'*n # setting difficulty up to 18 zeroes
    print(f"Mining  for  block initialized for difficulty : {n}  ")
    blockdata = block[:8]  # slicing data up to nonce and make a string
    block_string = ''.join(map(str, blockdata))  # converting list to string to hash
    tempnonce = 0
    flag = True  # to stop loop
    while flag:
        result = block_string + str(tempnonce)
        hash_object = hashlib.sha256(result.encode())  # creating hash object with string data
        hash_bytes = hash_object.digest()  # calculating hash
        result_hash_string = ''.join(f'{byte:08b}' for byte in hash_bytes)  # result the hash in string
        # now we have to check the nonce is right or not
 
        if result_hash_string[:n] == difficulty:  # comparing first 18 bits with difficulty
            flag = False
        else:
            tempnonce += 1  # increase the nonce

    return tempnonce
```
    
for Broadcasting block to the network
``` python
 ip_list = ['169.254.107.114'] ##reciver node ips
    port_block = 36361
    for ip in ip_list:
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ##creating socket for connection 
      try: 
        client_socket.connect((ip, port_block))# Connect to the server
        json_data = json.dumps(block[:12])# converting string to jason upto 12 lenght 
        client_socket.sendall(json_data.encode('utf-8')) ##sending data to server in bit
        print(f"Block sent successfully to {ip}:{port_block}")
      except Exception as e:
        print(f"Failed to send block to {ip}:{port_block}: {e}")
      finally:  
        client_socket.close()
```
for appending block in the blockchain
``` python
    blockchain.append(block)
    print(f"{node_name} created the {blockcounter_value}th block & added to Block chain successfully & is given below")
    #remove transection
    rmv_usd_trscn(block,mempool)
    blockcounter.value+=1
```    
for adding block to the database
```python
```
## Configuration

- Difficulty: we can adjust the difficulty of mining.
- Node count: we can add as many nodes as we want without any issue.
- block chain database: we can store the blockchain data in the database which is already integrated with the program.

## Contact

- phone no.1 : 7807860669 
    
- mail: xarthak@proton.me

- Phone no.2 : 8894128826

