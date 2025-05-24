# Libraries ## 3 rd of july
import sqlite3
import hashlib
import multiprocessing
import socket  
import json    
from datetime import datetime
import time
import random
import string
node_name = ''


#--------------------------------------------------------------------------Node code/wrapers of process 1----------------------------------------------------------------------------------
### node code 
def generate_transection():
    letters = string.ascii_letters  # includes lowercase and uppercase letters
    result_str = ''.join(random.choice(letters) for _ in range(20))
    return result_str
#remove transection code take boke, checks transection, remove from mempool
def rmv_usd_trscn (block,mempool):
   print('Transection below Removed from Mempool:-')
   for i in range (3,8):
      if block[i] == 'no transection':
         print('no transection are removed')
      else:
         temp=mempool.pop(block[i])
         print(f'{temp} revoved from mempool')
   time.sleep(1.5)
   
def printblock(blockchain,blockcounter):
    
    
    blockcounter_value = blockcounter.value -1
    print(f"Data of {blockcounter_value+1}th block:-")
    print("BLOCK HEADER")
    print(f"Block no.: {blockcounter_value+1}")
    print(f"Previous hash: {blockchain[blockcounter_value][0] if blockcounter_value >= 0 else 'None'}")
    print(f"Time of creation: {blockchain[blockcounter_value][1] if blockcounter_value >= 0 else 'None'}")
    print(f"Difficulty target: ")
    print(f"Nonce after mining: {blockchain[blockcounter_value][8] if blockcounter_value >= 0 else 'None'}")
    print(f"Current hash: {blockchain[blockcounter_value][9] if blockcounter_value >= 0 else 'None'}")
    print(f'Time took to mine {blockcounter_value}th block : {blockchain[blockcounter_value][10]}')
    print("Block Transaction details")
    for i in range(2, 8):
        print(blockchain[blockcounter_value][i] if blockcounter_value >= 0 else 'None')

#mining
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


def create_block (p2_terminate_event,blockchain,mempool,blockcounter,balance,difficulty,node_name):
    print('Creation of block started')
    time.sleep(0.5)
    blockcounter_value =  blockcounter.value
    block = [None] * 12  # prevhash, time of creation initiated, block reward, transaction 5, nonce, current hash,time at which block mined,block no.
   
    if blockcounter_value == 0:  #forr genesis block
        block[0] = '0' * 256  # previous hash with256 zeroes
        print('Gnenesis block creation initiated')
    else:
        
        block[0] = blockchain[blockcounter_value - 1][9]  # reference to previous block hash
        print(f'{blockcounter_value+1}th block creation initiated')
    #adding 5 random  transactions to the block       
    if len(mempool)>=5:
          transections=random.sample(list(mempool.keys()), 5) #taking random items 
          print(f"Transection selected are: {transections}")
          time.sleep(0.5)
          for i in range(3, 8):
            block[i] = transections[i-3]          
    else:
          print('Mempool has not enough transection for mining,Block is created using Empty transection')
          for i in range(3, 8):
            block[i] = 'no transection'           
    # block reward
    block[2] = f"{node_name} is rewarded with 5 Chip! to mine {blockcounter_value+1}th block "       
    # add creation time
    current_time = datetime.now().time()
    time_str = current_time.strftime('%H:%M:%S')
    block[1] = time_str
    # calculating nonce-----------mine
    block[8] = mine(block,difficulty)
    
    time_mine= datetime.now().time()
    time_str2 = time_mine.strftime('%H:%M:%S')
    block[10]=time_str2##time took to  mine

    #-------------------------------------------------------------------stop process paraya block
    p2_terminate_event.set()#set the flag to terminate the another process
    
    print(f"{blockcounter_value+1}th block mined successfully with nonce: {block[8]}" )
    time.sleep(0.2)
    print(f"{node_name} get 5 Chip! for mining" )
    time.sleep(0.2)
    print('Process of Paraya Block stops')

    #reward for ming
    
  
    balance.value +=5
    print(f'{balance.value} is the new balance of {node_name}' )
    
    #ading block no. atr last of block to recognise the block when sended
    block[11]= blockcounter_value+1
    # now putting the current hash element of block
    block_data_string = ''.join(map(str, block[:9]))
    hash_object = hashlib.sha256(block_data_string.encode())
    hash_bytes = hash_object.digest()
    block[9] = ''.join(f'{byte:08b}' for byte in hash_bytes)
    #send block to network 
    ip_list = ['192.168.1.10','192.168.1.20','192.168.1.40','192.168.1.50']   ##reciver node ips
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
    #adding block to block chain

    
    blockchain.append(block)
    
    print(f"{node_name} created the {blockcounter_value}th block & added to Block chain successfully & is given below")
    #remove transection
    rmv_usd_trscn(block,mempool)
    blockcounter.value+=1
    
    print(f'new block counter value {blockcounter.value}')
    
    time.sleep(0.5)



def paraya_block (p1_terminate_event,recev_blk_list,blockchain,mempool,blockcounter):#block check, verify , append
    print('Checking Paraya Block Initiated')
    time.sleep(0.5)
    flag = True
    while flag:
      ##check block
      
      if len(recev_blk_list)>0:
        
       for i in range(0,len(recev_blk_list)) :
        if recev_blk_list[i][11]== blockcounter.value+1:##checking block is the next one then the block counter
          print('next block found verifying it:-')
          #check last hash of block chain is equal to prev hash of receved block
          #CHECKING HASH 
          #print(f'{blockcounter}')
          blockcounterVALUE = blockcounter.value
          if  blockcounterVALUE == 0 and recev_blk_list[i][0]== '0'*256:
             print('prev hash for genesis block verified')
          elif recev_blk_list[i][0]== blockchain[ blockcounterVALUE-1][9]:
             print(f'previous hash for {blockcounter.value} is verified')
          else:
             continue
          #verify transection
          redflag=True
          for j in range(3,8):
             if recev_blk_list[i][j] not in mempool and recev_blk_list[i][j] != 'no transection' :
               redflag=False
          if redflag==False:
            print('transection not verified')
            continue
          else:
            print('transection verified')
          print('Block is verified')
          #----------------------------------stop process mine
          p1_terminate_event.set()
          print('process mining is stoped and given block is added to block chain')
          #append block 
          blockchain.append(recev_blk_list[i])
          blockcounter.value+=1
          print(f'new block counter value {blockcounter.value}')
          #remove transection from mempool
          rmv_usd_trscn(recev_blk_list[i],mempool)
          recev_blk_list.pop(i)
          flag=False
          break
        else:
          recev_blk_list.pop(i) 
def node(blockchain, blockcounter, balance, mempool, recev_blk_list,difficulty,node_name):
   
   print(f'**{node_name} A started**')#node initiated
   for _ in range (5):
        
    for _ in range(3):
     transection = generate_transection()
     mempool.update({transection:transection})# update the mempool with our generate transection
     print(f"broadcasting transection:'{transection}' to all nodes ")

     #---sending transection to node via port 56561---

     ip_list = ['192.168.1.10','192.168.1.20','192.168.1.40','192.168.1.50']   ##reciver node ips'169.254.6.64','169.254.213.200',
     port_trnsction = 56561
     for ip in ip_list:
       time.sleep(0.001)
       client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ##creating socket for connection 
       try: 
        client_socket.connect((ip, port_trnsction))# Connect to the server
        json_data = json.dumps(transection)# converting string to jason 
        client_socket.sendall(json_data.encode('utf-8')) ##sending data to server in bit
       # print(f"Data sent successfully to {ip}:{port_trnsction}")
       except Exception as e:
         print(f"Failed to send data to {ip}:{port_trnsction}: {e}")
       finally:  
         client_socket.close()
    print('transection sent successfully')
    time.sleep(1)
    p1_terminate_event = multiprocessing.Event()
    p2_terminate_event = multiprocessing.Event()
    #Block creation & parallel block checking 
    p2_paraya_blk =multiprocessing.Process(target=paraya_block, args=(p1_terminate_event,recev_blk_list,blockchain,mempool,blockcounter,))
    p1_mine = multiprocessing.Process(target=create_block,args=(p2_terminate_event,blockchain,mempool,blockcounter,balance,difficulty,node_name,))
    
    # starting processes
    p2_paraya_blk.start()
    p1_mine.start()
    
    
    while not p1_terminate_event.is_set() and not p2_terminate_event.is_set(): #check which is completed first
        time.sleep(0.0001)
    
    if p1_terminate_event.is_set():
        p1_mine.terminate()
        print('Process of Mining terminated succesfully')
    if p2_terminate_event.is_set():
        p2_paraya_blk.terminate()
        print('Paraya block process terminated successfully')
    
    p1_mine.join()# wait to free resources
    p2_paraya_blk.join()#wait to free resorces
    
    
    printblock(blockchain,blockcounter)
      
    
 #------------------------------------------recieve block--------------------------------------------
def rcv_blk_server(recev_blk_list,node_name):
   print(f"Recieve Block server for {node_name} started and listening on Port  36361")
   
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.bind(('', 36361))#bind to the interface and port of server
   server_socket.listen(30)#how many req can quede up
   while True:
        client_socket, client_address = server_socket.accept()
       

        try:
            data = b""
            while True:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                data += packet

            # Decode received bytes to UTF-8 string
            json_data = data.decode('utf-8')
            # Parse jason strig inot the recieved block
            paraya_blk = json.loads(json_data)
            # append the block in recieev block
            recev_blk_list.append(paraya_blk)
            print(f"Recieved block from {client_address} : {paraya_blk}")
        except Exception as e:
            print(f"Failed to receive data from {client_address}: {e}")

        finally:
            client_socket.close()
            print(f"Connection with {client_address} closed")
 
 #------------------------------------------recieve transection--------------------------------------
def rcv_trnsctn_server(mempool,node_name):
   print(f"Recieve BlockTransection server for {node_name} started and listening on Port  56561")
   
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.bind(('',56561))#bind to the interface and port of server
   server_socket.listen(30)#how many req can quede up
   while True:
        client_socket, client_address = server_socket.accept()
       

        try:
            data = b""
            while True:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                data += packet

            # Decode received bytes to UTF-8 string
            json_data = data.decode('utf-8')
            # Parse jason strig inot the recieved transection
            rcv_trnsctn = json.loads(json_data)
            # append the transection string in mempool
            mempool.update({rcv_trnsctn:rcv_trnsctn})
            print(f"transection from {client_address} recieved: {rcv_trnsctn}")
        except Exception as e:
            print(f"Failed to receive data during trnsection recieve from {client_address}: {e}")

        finally:
            client_socket.close()
            print(f"Connection with {client_address} closed trnsection")
            
#-------------driver code----------------------------------------------------------------
def main():
  global node_name
  node_name=input('eneter node name :')
  
   #********************
                                                                         #DATASTRUCTURE

 #creating a manager to to manage shared recoureces while multi processing                                                                         
  manager = multiprocessing.Manager()
 # creating the personal ledger
  blockchain= manager.list()
 #personal wallet balance
  balance = manager.Value('i', 0)
 #mempool for transection that are recieved by the transection reciever our
  mempool =manager.dict()  # have transaction
  recev_blk_list = manager.list()
  blockcounter = manager.Value('i', 0) 
 #data base for the blockchain --------------------------------------------------
 #connect to the file\data base
  conn = sqlite3.connect('BlockChain_db.db')
  cursor = conn.cursor()# create a cursor to traverse the table
  cursor.execute('''CREATE TABLE IF NOT EXISTS BLOCKCHAIN (
                    PREVIOUS_HASH TEXT,
                    TIME_OF_CREATION TEXT,
                    BLOCK_REWARD TEXT,
                    TRANSACTION_1 TEXT,
                    TRANSACTION_2 TEXT,
                    TRANSACTION_3 TEXT,
                    TRANSACTION_4 TEXT,
                    TRANSACTION_5 TEXT,
                    NONCE INTEGER,
                    CURRENT_HASH TEXT,
                    TIME_TO_MINE TEXT,
                    BLOCK_NO INTEGER
                )''')
  # Execute a query to count rows in the table
  cursor.execute('SELECT * FROM BLOCKCHAIN ')
  # Fetch the result
  start_rows = cursor.fetchall()
  count = len(start_rows)
  print(f'count:{count}')
  if count==0:
     print('STARTING THE DATA BASE')
  else:
     print('continuing old block chain')
     #move data to block chain 
     # Example SELECT query to retrieve all data from mytable
     cursor.execute('SELECT * FROM BLOCKCHAIN')

    # Fetch all rows as a list of tuples
     rows = cursor.fetchall()
    # Convert list of tuples to a 2D list (list of lists)
     data = [list(row) for row in rows]
     for row in data:
        blockchain.append(row)
     
     blockcounter.value = count
     
 
  print(f'new block counter value {blockcounter.value}')
 #----------------------------------------
  p_trns_srvr=multiprocessing.Process(target=rcv_trnsctn_server, args=(mempool,node_name,))
  p_block_srvr=multiprocessing.Process(target=rcv_blk_server, args=(recev_blk_list,node_name,))
  p_trns_srvr.start()
 
  p_block_srvr.start()
  time.sleep(0.5)
  difficulty = int(input('enter diificulty :'))
  p_node=multiprocessing.Process(target=node,args=(blockchain, blockcounter, balance, mempool, recev_blk_list,difficulty,node_name,))
  p_node.start()
  
  ##wait to end
  p_node.join()
  

  ## add the new data in the data base block chain
  for row in blockchain[count:]:
    try:
       
            # Execute INSERT statement to add row to BLOCKCHAIN table
        cursor.execute('INSERT INTO BLOCKCHAIN (PREVIOUS_HASH, TIME_OF_CREATION, BLOCK_REWARD, TRANSACTION_1, TRANSACTION_2, TRANSACTION_3, TRANSACTION_4, TRANSACTION_5, NONCE, CURRENT_HASH, TIME_TO_MINE, BLOCK_NO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
        # Commit changes after all insertions are done
       
        print('Data inserted into database successfully')
    except Exception as e:
        print(f'Error inserting data: {e}')
  conn.commit()
# Now fetch and print the data from the BLOCKCHAIN table
  cursor.execute('SELECT * FROM BLOCKCHAIN')
  time.sleep(1.5)
# Fetch all rows as a list of tuples
  rows = cursor.fetchall()

# Print table headers
  cursor.execute('PRAGMA table_info(BLOCKCHAIN)')
  columns = [row[1] for row in cursor.fetchall()]
  print("Table Columns:", columns)

# Print fetched rows
  print("Fetched Rows:")
  for row in rows:
    print(row)

  cursor.close()
  conn.close()
  print('program reches end, close terminal to close server')  #terminate server after node completion
  p_block_srvr.terminate()
  p_trns_srvr.terminate()
  p_block_srvr.join()
  p_trns_srvr.join()  
  

if __name__=="__main__":
    main()