from cryptography.fernet import Fernet 

key = Fernet.generate_key()

temp = Fernet(key)
name = "hello123"
# token = temp.encrypt(b"rishabh13454")
token = temp.encrypt(name.encode())


print("encrypted key: "+str(token))

new_text = temp.decrypt(token).decode()
print(new_text) 