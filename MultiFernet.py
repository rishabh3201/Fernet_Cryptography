from cryptography.fernet import Fernet, MultiFernet

key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())

final = MultiFernet([key1,key2])
password = "hello123"
temp = final.encrypt(password.encode())
print(temp)

key3 = Fernet(Fernet.generate_key())
final = MultiFernet([key3, key1,key2])
rotated = final.rotate(temp)
new_text = final.decrypt(rotated).decode()
print(new_text)