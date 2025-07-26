import paramiko


host = "sciring.in"
user = "root"
password = "wrog"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=host, username=user , password=password, timeout=3)
    print(f"the connection was successful with {host}")

except Exception as e:
    print(f" the connnection was failed with {host}")