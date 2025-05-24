# 🔗 Blockchain Construction and Analysis of Consensus Algorithm

This project presents a fully functional blockchain system built from scratch in Python. It includes peer-to-peer networking, a transaction pool, mining via Proof of Work (PoW), and detailed analysis of consensus mechanisms. The system supports scalable deployment with multiple full nodes and offers insights into how difficulty affects mining behavior, performance, and security.

---

## 📚 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contact](#contact)
- [Acknowledgement](#acknowledgement)

---

## 🧾 Introduction

This project simulates a basic cryptocurrency system that reflects the core principles behind blockchain and mining. A peer-to-peer system is created where multiple full nodes participate in transaction validation and block mining. It also includes an in-depth analysis of the Proof of Work (PoW) consensus algorithm, studying its impact on mining difficulty and security.

---

## ✨ Features

- ✅ **Full Nodes**: Every node is a full node capable of mining and storing the entire blockchain.
- 🧾 **Transaction Pool (Mempool)**: Collects and validates transactions before mining.
- ⛏️ **Proof of Work Mining**: Implements a basic PoW algorithm with difficulty adjustment and nonce discovery.
- 📡 **Block Broadcasting**: Newly mined blocks are broadcasted to all connected nodes.
- 📈 **Scalable Architecture**: Easily scalable to multiple nodes with minor configuration.
- 🔐 **Blockchain Integrity**: Ensures immutability and synchronization across nodes.
- 🧪 **Performance Analysis**: Observes real-world behavior and trade-offs in consensus mechanisms.

---

## 💻 Installation

1. **Install VS Code**  
   Download from: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

2. **Install Python Extension in VS Code**  
   ![Python Extension](https://imgs.search.brave.com/-0CybY4nT54KhgD8lRSuJMMJgvT3bDIcQYXHwKGx5M4/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9saWdo/dHJ1bi5jb20vd3At/Y29udGVudC91cGxv/YWRzLzIwMjMvMDMv/cHl0aG9uX2Zvcl92/c2NvZGUucG5n)

3. **Install Python Libraries**  
   Required built-in libraries:
   - `hashlib`
   - `multiprocessing`
   - `socket`
   - `json`
   - `datetime`
   - `time`
   - `random`
   - `string`

---

## 🌐 Setup

- Connect all nodes using Wi-Fi or a switch.
- Allow file sharing and network permissions on each system.
- Verify connections using `ping` command (see tutorial):  
  [Watch Tutorial](https://youtu.be/CGeAauny2fc?si=Whea1SzorUv5BNm5)

![Ping Command](https://imgs.search.brave.com/8Vw1r-0jflfNXzH1W1ctvrgzj9ZonH_GR_CeSiCbofw/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9ibG9n/LmludmdhdGUuY29t/L2hzLWZzL2h1YmZz/L3BpbmctY29tbWFu/ZC1zeW50YXgtZXhh/bXBsZS0yLnBuZz93/aWR0aD02ODAmaGVp/Z2h0PTMxMCZuYW1l/PXBpbmctY29tbWFu/ZC1zeW50YXgtZXhh/bXBsZS0yLnBuZw)

- Disable firewalls if connections fail.

---

## 🛠️ Usage

1. Run the Python file on each node using VS Code.
2. Input:
   - Node name
   - Mining difficulty (same across all nodes)

### 🔄 Example Functions

**Transaction Generator**
```python
def generate_transection():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(20))
Mining Algorithm

python
Copy
Edit
def mine(block, difficulty):
    difficulty_str = '0' * difficulty
    ...
    while True:
        result = block_string + str(tempnonce)
        hash_object = hashlib.sha256(result.encode())
        hash_string = ''.join(f'{byte:08b}' for byte in hash_object.digest())
        if hash_string.startswith(difficulty_str):
            break
        tempnonce += 1
    return tempnonce
```
Broadcasting Block

```python
for ip in ip_list:
    try:
        client_socket.connect((ip, port_block))
        json_data = json.dumps(block[:12])
        client_socket.sendall(json_data.encode('utf-8'))
```
Appending Block

```python
blockchain.append(block)
rmv_usd_trscn(block, mempool)
blockcounter.value += 1
```
⚙️ Configuration
Difficulty: Adjustable per experiment.

Node Count: Easily extendable to N nodes.

Database: Blockchain data can be saved persistently.

📬 Contact
📞 Phone 1: 7807860669

📧 Email: xarthak@proton.me

📞 Phone 2: 8894128826

🙏 Acknowledgement
Special thanks to all those who contributed to this experimental and educational endeavor, and to the open-source Python community for making such implementations possible.

